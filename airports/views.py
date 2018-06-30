from django.shortcuts import render, get_object_or_404
from .models import Airport, Runway, AirportComm

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import AirportSerializer, RunwaySerializer, AirportCommSerializer


class AirportViewSet(ViewSet):
    """
    DRF Viewset for Airport objects
    """

    def list(self, request):
        queryset = Airport.objects.all()
        serializer = AirportSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Airport.objects.all()
        airport = get_object_or_404(queryset, pk=pk)
        serializer = AirportSerializer(airport)
        return Response(serializer.data)


class RunwayViewSet(ViewSet):
    """
    DRF Viewset for Runway objects
    """

    def list(self, request):
        queryset = Runway.objects.all()
        serializer = RunwaySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Runway.objects.all()
        runway = get_object_or_404(queryset, pk=pk)
        serializer = RunwaySerializer(runway)
        return Response(serializer.data)


class AirportCommViewSet(ViewSet):
    """
    DRF Viewset for AirportComm objects
    """

    def list(self, request):
        queryset = AirportComm.objects.all()
        serializer = AirportCommSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = AirportComm.objects.all()
        airport_comm = get_object_or_404(queryset, pk=pk)
        serializer = AirportCommSerializer(airport_comm)
        return Response(serializer.data)
