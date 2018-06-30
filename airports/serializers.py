from rest_framework.serializers import ModelSerializer
from .models import Airport, Runway, AirportComm


class AirportSerializer(ModelSerializer):
    class Meta:
        model = Airport
        fields = ('icao', 'name', 'region', 'elevation', 'metar', 'taf', 'sunrise', 'sunset')


class RunwaySerializer(ModelSerializer):
    class Meta:
        model = Runway
        fields = ('airport', 'name', 'surface_type', 'length', 'width', 'bearing')


class AirportCommSerializer(ModelSerializer):
    class Meta:
        model = AirportComm
        fields = ('frequency', 'airport', 'type')
