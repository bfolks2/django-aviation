from django.db import models


class Airport(models.Model):

    icao = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=256)
    region = models.CharField(max_length=32)
    elevation = models.IntegerField(help_text='MSL, feet')

    # Dynamic values altered per GET request
    metar = models.CharField(max_length=512, blank=True, null=True)
    taf = models.CharField(max_length=1024, blank=True, null=True)
    sunrise = models.DateTimeField(max_length=64, blank=True, null=True)
    sunset = models.DateTimeField(max_length=64, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.icao = self.icao.upper()
        super(Airport, self).save(*args, **kwargs)

    def __str__(self):
        return u'{} - {}'.format(self.name, self.icao.upper())


class Runway(models.Model):

    ASP = 1
    CON = 2
    GRS = 3
    OTHER = 4

    SURFACE_CHOICES = (
        (ASP, 'Asphalt'),
        (CON, 'Concrete'),
        (GRS, 'Grass'),
        (OTHER, 'Other')
    )

    airport = models.ForeignKey('airports.Airport')
    name = models.CharField(max_length=32)
    surface_type = models.IntegerField(choices=SURFACE_CHOICES, default=ASP)
    length = models.DecimalField(max_digits=7, decimal_places=2, help_text='Length in feet')
    width = models.DecimalField(max_digits=7, decimal_places=2, help_text='Width in feet')
    bearing = models.CharField(max_length=13, help_text='Bearing in degrees')

    def __str__(self):
        return u'{} - {}'.format(self.airport.icao, self.name)


class AirportComm(models.Model):

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

    frequency = models.DecimalField(max_digits=6, decimal_places=3)
    airport = models.ForeignKey('airports.Airport')
    type = models.IntegerField(choices=TYPE_CHOICES, default=CTAF)

    def __str__(self):
        return u'{} - {}'.format(self.airport.icao, self.frequency)
