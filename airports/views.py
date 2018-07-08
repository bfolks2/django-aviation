from rest_framework.decorators import action
from rest_framework.response import Response

from prepair.views import PrepairViewSet
from .models import Airport, Runway, AirportComm
from .serializers import AirportSerializer, RunwaySerializer, AirportCommSerializer

from api.flightplan_client import FlightPlanAPIClient


class AirportViewSet(PrepairViewSet):
    """
    DRF Viewset for Airport objects
    """

    prepair_model_class = Airport
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

    filter_fields = ('pk', 'icao', 'name', 'region', 'elevation')
    iexact_filter_fields = ('icao', 'name', 'region')

    @action(methods=['get'], detail=True, permission_classes=[])
    def airport_weather(self, request, pk=None):
        # If the window query is non-zero, the weather has already been updated and does not require
        # another GET request to the external API
        updated = int(request.GET.get('window', None))

        if not updated:
            try:
                airport = Airport.objects.get(pk=pk)
            except Airport.DoesNotExist:
                return False

            flight_client = FlightPlanAPIClient()
            pk = flight_client.get(icao=airport.icao)

        return Response({'pk': pk})


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
