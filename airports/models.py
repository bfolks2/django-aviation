from django.db import models


class Airport(models.Model):

    icao = models.CharField(max_length=4)
    name = models.CharField(max_length=256)
    region = models.CharField(max_length=32)
    elevation = models.IntegerField()

    # Dynamic values altered per GET request
    metar = models.CharField(max_length=512, blank=True, null=True)
    taf = models.CharField(max_length=1024, blank=True, null=True)
    sunrise = models.CharField(max_length=64, blank=True, null=True)
    sunset = models.CharField(max_length=64, blank=True, null=True)


class Runway(models.Model):

    ASP = 1
    CON = 2
    GRS = 3

    SURFACE_CHOICES = (
        (ASP, 'Asphalt'),
        (CON, 'Concrete'),
        (GRS, 'Grass'),
    )

    airport = models.ForeignKey('airports.Airport')
    name = models.CharField(max_length=32)
    surface_type = models.IntegerField(choices=SURFACE_CHOICES, default=ASP)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    width = models.DecimalField(max_digits=6, decimal_places=2)
    bearing = models.DecimalField(max_digits=5, decimal_places=2)


class Communication(models.Model):

    CTAF = 1
    UNICOM = 2
    ATIS = 3
    GROUND = 4
    TOWER = 5
    APPROACH = 6
    DEPARTURE = 7
    CLEARANCE = 8

    TYPE_CHOICES = (
        (CTAF, 'Common Traffic Advisory Frequency'),
        (UNICOM, 'Universal Communications'),
        (ATIS, 'Weather'),
        (GROUND, 'Ground'),
        (TOWER, 'Tower'),
        (APPROACH, 'Approach'),
        (DEPARTURE, 'Departure'),
        (CLEARANCE, 'Clearance'),
    )

    frequency = models.DecimalField(max_digits=5, decimal_places=2)
    airport = models.ForeignKey('airports.Airport')
    type = models.IntegerField(choices=TYPE_CHOICES, default=CTAF)
