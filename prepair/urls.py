"""prepair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from prepair import views

from airports.views import AirportViewSet, RunwayViewSet, AirportCommViewSet
from accounts.views import MemberViewSet, UserViewSet
from communication.views import PostViewSet, CommentViewSet

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index-view'),
    url(r'^redirect-icao$', views.redirect_icao, name='redirect-icao'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dashboard/?', views.DashboardTemplateView.as_view(), name='dashboard')
]

# Below are the DRF-Ember Router URL patterns

router = DefaultRouter(trailing_slash=False)
router.register(r'airports', AirportViewSet, base_name='serializers-airport')
router.register(r'runways', RunwayViewSet, base_name='serializers-runway')
router.register(r'airport-comms', AirportCommViewSet, base_name='serializers-airportcomm')
router.register(r'members', MemberViewSet, base_name='serializers-member')
router.register(r'users', UserViewSet, base_name='serializers-user')
router.register(r'posts', PostViewSet, base_name='serializers-post')
router.register(r'comments', CommentViewSet, base_name='serializers-comment')

serializer_patterns = [
    url(r'^serializers/', include(router.urls)),
]

urlpatterns += serializer_patterns
