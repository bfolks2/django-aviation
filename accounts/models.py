from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User)
    home_airport = models.ForeignKey('airports.Airport', blank=True, null=True)

    def __str__(self):
        return self.user.username
