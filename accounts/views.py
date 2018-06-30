from django.shortcuts import render, get_object_or_404
from .models import Member

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import MemberSerializer


class MemberViewSet(ViewSet):
    """
    DRF Viewset for Member objects
    """

    def list(self, request):
        queryset = Member.objects.all()
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Member.objects.all()
        member = get_object_or_404(queryset, pk=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)
