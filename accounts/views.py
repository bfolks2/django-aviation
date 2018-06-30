from django.shortcuts import render, get_object_or_404

from prepair.views import PrepairViewSet
from .models import Member
from .serializers import MemberSerializer


class MemberViewSet(PrepairViewSet):
    """
    DRF Viewset for Member objects
    """

    prepair_model_class = Member
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    filter_fields = ('pk', 'user', 'home_airport')
    iexact_filter_fields = tuple()
