from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import AirportViewSet, RunwayViewSet, AirportCommViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'airports', AirportViewSet, base_name='serializers-airport')
router.register(r'runways', RunwayViewSet, base_name='serializers-runway')
router.register(r'airport-comms', AirportCommViewSet, base_name='serializers-airportcomm')

urlpatterns = [
    url(r'^serializers/', include(router.urls)),
]
