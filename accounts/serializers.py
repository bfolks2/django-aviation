from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Member


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ('pk', 'user', 'home_airport')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username')
