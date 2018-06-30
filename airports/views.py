from django.shortcuts import render, get_object_or_404

from prepair.views import PrepairViewSet
from .models import Airport, Runway, AirportComm
from .serializers import AirportSerializer, RunwaySerializer, AirportCommSerializer


class AirportViewSet(PrepairViewSet):
    """
    DRF Viewset for Airport objects
    """

    prepair_model_class = Airport
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

    filter_fields = ('pk', 'icao', 'name', 'region', 'elevation')
    iexact_filter_fields = ('icao', 'name', 'region')


class RunwayViewSet(PrepairViewSet):
    """
    DRF Viewset for Runway objects
    """

    prepair_model_class = Runway
    queryset = Runway.objects.all()
    serializer_class = RunwaySerializer

    filter_fields = ('pk', 'airport', 'name', 'surface_type')
    iexact_filter_fields = ('name',)


class AirportCommViewSet(PrepairViewSet):
    """
    DRF Viewset for AirportComm objects
    """

    prepair_model_class = AirportComm
    queryset = AirportComm.objects.all()
    serializer_class = AirportCommSerializer

    filter_fields = ('pk', 'frequency', 'airport', 'type')
    iexact_filter_fields = tuple()
