import requests
from airports.serializers import AirportSerializer, RunwaySerializer, AirportCommSerializer
from airports.models import Airport, Runway, AirportComm

from datetime import datetime

class FlightPlanAPIClient(object):
    """
    API Client class used to construct requests to FlightPlaneDatabase's Airport Information API
    """

    HOST = 'https://api.flightplandatabase.com/'

    AIRPORT_MAPPER = {
        'ICAO': 'icao',
        'name': 'name',
        'region': 'region',
        'elevation': 'elevation',
    }

    WEATHER_MAPPER = {
        'METAR': 'metar',
        'TAF': 'taf',
    }

    RUNWAY_MAPPER = {
        'ident': 'name',
        'surface': 'surface_type',
        'length': 'length',
        'width': 'width',
        'bearing': 'bearing'
    }

    COMM_MAPPER = {
        'type': 'type',
        'frequency': 'frequency'
    }

    passthrough_converter = {
        'COM': AirportComm.CTAF,
        'REC': AirportComm.ATIS,
        'GND': AirportComm.GROUND,
        'TWR': AirportComm.TOWER,
        'APP': AirportComm.APPROACH,
        'DEP': AirportComm.DEPARTURE,
        'CLD': AirportComm.CLEARANCE
    }

    def __init__(self, *args, **kwargs):
        self.http_session = requests.Session()

    def get(self, icao):
        url = u'{}nav/airport/{}'.format(self.HOST, icao)

        headers = {
            'Authorization': 'KM2iNdFY4lVKtHTiwsqEP40Wgarbm4z9MAbEVWqY',
            'Accept': 'application/json',
            'X-Units': 'AVIATION',
        }

        response = self.http_session.get(url, headers=headers)
        json = response.json()

        icao_db = icao.upper()
        query = Airport.objects.filter(icao=icao_db)

        # If an Airport already exists, get it.  Otherwise create it and all its Foreign Key relations
        if query.exists():
            airport = query.get()
        else:
            airport = self.create_airport(json)

        if not airport:
            return None

        weather_data = self.set_weather_data(json)
        if weather_data:
            Airport.objects.filter(pk=airport.pk).update(**weather_data)

        # Return the updated Airport pk to the view to handle the details page
        return airport.pk

    def create_airport(self, json):

        data = self.field_mapper_logic(self.AIRPORT_MAPPER, json)

        airport_serializer = AirportSerializer(data=data)
        if airport_serializer.is_valid(raise_exception=False):
            airport = Airport.objects.create(**airport_serializer.validated_data)

            # With the newly created airport, also create Runway and AirportComm objects
            self.create_runways(airport, json)
            self.create_airport_comms(airport, json)

            return airport

        return None

    def create_runways(self, airport, json):

        for runway_data in json['runways']:
            data = self.field_mapper_logic(self.RUNWAY_MAPPER, runway_data)
            data.update({'airport': airport.pk})
            data = self.runway_field_validator(data)

            runway_serializer = RunwaySerializer(data=data)
            if runway_serializer.is_valid(raise_exception=False):
                Runway.objects.get_or_create(**runway_serializer.validated_data)

        return

    def create_airport_comms(self, airport, json):

        for airport_comm_data in json['frequencies']:
            data = self.field_mapper_logic(self.COMM_MAPPER, airport_comm_data)
            data.update({'airport': airport.pk})
            data = self.airport_comm_field_validator(data)

            airport_comm_serializer = AirportCommSerializer(data=data)
            if airport_comm_serializer.is_valid(raise_exception=False):
                AirportComm.objects.get_or_create(**airport_comm_serializer.validated_data)

        return

    def runway_field_validator(self, data):
        # These fields come in from the API in raw format
        strings_to_decimals = ['length', 'width', 'bearing']
        for field in strings_to_decimals:
            value = data[field]
            converted_value = round(float(value), 2)
            data[field] = converted_value

        # Convert API values to Django Field Choices
        runway_dict = dict(Runway.SURFACE_CHOICES)
        for key in runway_dict:
            if runway_dict[key].lower() == data['surface_type'].lower():
                data['surface_type'] = key
                break

        return data

    def airport_comm_field_validator(self, data):
        strings_to_decimals = ['frequency']
        for field in strings_to_decimals:
            value = data[field]
            converted_value = round(float(value/1000000), 2)
            data[field] = converted_value

        # Convert API values to Django Field Choices
        # Requires extra conversion to convert from API raw value to clean Django Choice
        for key in self.passthrough_converter:
            if key == data['type'].upper():
                data['type'] = self.passthrough_converter[key]
                return data

        # If not matches, set as UNICOM
        data['type'] = AirportComm.UNICOM
        return data

    def set_weather_data(self, json):
        # Once an airport is set, update the weather on this airport based on the current data
        weather_data = json['weather']
        data = self.field_mapper_logic(self.WEATHER_MAPPER, weather_data)
        data = self.weather_field_validator(data)

        # Get sunrise/sunset values from API raw data and convert to DateTime
        # We must remove the trailing Zulu and mid-line T from the API raw_value
        raw_sunset = json['times'].get('sunset', None)
        if raw_sunset:
            sunset = datetime.strptime(raw_sunset[:-1].replace('T', ' '), '%Y-%m-%d %H:%M:%S.%f')
            data['sunset'] = sunset.replace(second=0, microsecond=0)

        raw_sunrise = json['times'].get('sunrise', None)
        if raw_sunrise:
            sunrise = datetime.strptime(raw_sunrise[:-1].replace('T', ' '), '%Y-%m-%d %H:%M:%S.%f')
            data['sunrise'] = sunrise.replace(second=0, microsecond=0)

        return data


    @staticmethod
    def weather_field_validator(data):
        metar = data['metar']
        taf = data['taf']

        metar_length = 512
        if not metar:
            data.pop('metar', None)
        elif len(metar) > metar_length:
            data['metar'] = metar[:(metar_length-3)] + '...'

        taf_length = 1024
        if not taf:
            data.pop('taf', None)
        elif len(taf) > taf_length:
            data['taf'] = taf[:(taf_length - 3)] + '...'

        return data

    @staticmethod
    def field_mapper_logic(field_mapper, json):
        data = {}

        for field in field_mapper:
            if field in json:
                data[field_mapper[field]] = json[field]

        return data
