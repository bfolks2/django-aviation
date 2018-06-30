from rest_framework.serializers import ModelSerializer
from .models import Airport, Runway, AirportComm


class AirportSerializer(ModelSerializer):
    class Meta:
        model = Airport
        fields = ('pk', 'icao', 'name', 'region', 'elevation', 'metar', 'taf', 'sunrise', 'sunset')


class RunwaySerializer(ModelSerializer):
    class Meta:
        model = Runway
        fields = ('pk', 'airport', 'name', 'surface_type', 'length', 'width', 'bearing')


class AirportCommSerializer(ModelSerializer):
    class Meta:
        model = AirportComm
        fields = ('pk', 'frequency', 'airport', 'type')
