from django.shortcuts import render, get_object_or_404

from prepair.views import PrepairViewSet
from .models import Airport, Runway, AirportComm
from .serializers import AirportSerializer, RunwaySerializer, AirportCommSerializer


class AirportViewSet(PrepairViewSet):
    """
    DRF Viewset for Airport objects
    """

    DB_MODEL_CLASS = Airport
    SERIALIZER_CLASS = AirportSerializer


class RunwayViewSet(PrepairViewSet):
    """
    DRF Viewset for Runway objects
    """

    DB_MODEL_CLASS = Runway
    SERIALIZER_CLASS = RunwaySerializer


class AirportCommViewSet(PrepairViewSet):
    """
    DRF Viewset for AirportComm objects
    """

    DB_MODEL_CLASS = AirportComm
    SERIALIZER_CLASS = AirportCommSerializer
