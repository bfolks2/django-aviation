from django.contrib import admin
from .models import Airport, Runway, AirportComm


class AirportAdmin(admin.ModelAdmin):
    list_display = ('icao', 'name', 'region', 'elevation')
    search_fields = ['icao', 'name']


class RunwayAdmin(admin.ModelAdmin):
    list_display = ('airport', 'name', 'surface_type')
    search_fields = ['airport__icao', 'airport__name', 'name']


class AirportCommAdmin(admin.ModelAdmin):
    list_display = ('airport', 'frequency', 'type')
    search_fields = ['airport__icao', 'airport__name', 'frequency', 'type']


admin.site.register(Airport, AirportAdmin)
admin.site.register(Runway, RunwayAdmin)
admin.site.register(AirportComm, AirportCommAdmin)
