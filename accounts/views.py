from django.shortcuts import render, get_object_or_404

from prepair.views import PrepairViewSet
from .models import Member
from .serializers import MemberSerializer


class MemberViewSet(PrepairViewSet):
    """
    DRF Viewset for Member objects
    """

    DB_MODEL_CLASS = Member
    SERIALIZER_CLASS = MemberSerializer
