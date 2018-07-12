from django.shortcuts import render
from django.http.request import QueryDict
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from six.moves.urllib.parse import urlparse

from rest_framework.viewsets import GenericViewSet as DRFGenericViewset
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from api.flightplan_client import FlightPlanAPIClient
from accounts.models import Member


def index(request):
    user = request.user
    data = {}

    if user.id:
        try:
            member = Member.objects.get(user=user)
            home_airport_pk = member.home_airport.pk
            home_airport_icao = member.home_airport.icao
            data = {'home_airport_pk': home_airport_pk, 'home_airport_icao': home_airport_icao}
        except Member.DoesNotExist:
            pass  # Data error, do not return empty dictionary
        except Member.MultipleObjectsReturned:
            pass  # Data error, do not return empty dictionary

    return render(request, 'index.html', data)


def redirect_icao(request):
    icao = request.POST.get('icao', None)

    client = FlightPlanAPIClient()
    pk = client.get(icao=icao.lower())

    return HttpResponseRedirect(reverse('dashboard') + '/?airportpk={}'.format(pk))


class DashboardTemplateView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardTemplateView, self).get_context_data(**kwargs)

        airport_pk = self.request.GET.get('airportpk', 0)
        user_id = self.request.user.id if self.request.user.id else 0
        if urlparse(self.request.path).path == '/dashboard/':
            base_redirect = 1
        else:
            base_redirect = 0

        context['airport_pk'] = airport_pk
        context['user_id'] = user_id
        context['base_redirect'] = base_redirect

        return context


class PrepairViewSet(CreateModelMixin,
                     ListModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     DRFGenericViewset):
    """
    Base DRF Viewset for all objects
    Default CRUD Methods are all inherited through DRF Mixins
    """

    # These values are set within the subclass Model Viewsets
    prepair_model_class = None
    queryset = None
    serializer_class = None

    filter_fields = tuple()
    iexact_filter_fields = tuple()

    def filter_queryset(self, queryset=None, is_list_call=False):
        request_params = self.request.query_params

        filter_kwargs = {}
        for filter_field in self.filter_fields:
            if filter_field in request_params:
                initial_filter_field = filter_field

                if isinstance(request_params, QueryDict):
                    values_list = request_params.getlist(filter_field)
                else:
                    values_list = request_params.get(filter_field)

                # Django ORM does not support iexact__in, so must choose one or the other
                if isinstance(values_list, list) and len(values_list) > 1:
                    filter_kwargs[filter_field + '__in'] = values_list
                else:
                    if filter_field in self.iexact_filter_fields:
                        filter_field += '__iexact'
                    filter_kwargs[filter_field] = request_params[initial_filter_field]

        return self.prepair_model_class.objects.filter(**filter_kwargs)
