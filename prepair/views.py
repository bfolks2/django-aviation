from django.shortcuts import render
from django.http.request import QueryDict
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.conf import settings

from rest_framework.viewsets import GenericViewSet as DRFGenericViewset
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from api.flightplan_client import FlightPlanAPIClient


def index(request):
    return render(request, 'index.html')


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
        username = self.request.user.username if self.request.user.username else 0

        context['airport_pk'] = airport_pk
        context['user_id'] = user_id

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
