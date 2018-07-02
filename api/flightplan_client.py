import requests
from airports.serializers import AirportSerializer
from airports.models import Airport


class FlightPlanAPIClient(object):
    """
    API Client class used to construct requests to FlightPlaneDatabase's Airport Information API
    """

    HOST = 'https://api.flightplandatabase.com/'

    FIELD_MAPPER = {
        'ICAO': 'icao',
        'name': 'name',
        'region': 'region',
        'elevation': 'elevation',
    }

    WEATHER_MAPPER = {
        'METAR': 'metar',
        'TAF': 'taf',
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

        if query.exists():
            airport = query.get()
        else:
            airport = self.create_airport(json)

        return airport

    def create_airport(self, json):

        data = {}

        for field in self.FIELD_MAPPER:
            if field in json:
                data[self.FIELD_MAPPER[field]] = json[field]

        airport_serializer = AirportSerializer(data=data)
        airport_serializer.is_valid(raise_exception=True)

        return Airport.objects.create(**airport_serializer.validated_data)

    def create_runways(self, airport_pk, json):
        pass

    def create_airport_comms(self, airport_pk, json):
        pass
