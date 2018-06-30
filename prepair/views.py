from django.shortcuts import render, get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


def index(request):
    return render(request, 'index.html')


class PrepairViewSet(ViewSet):
    """
    Base DRF Viewset for all objects to inherit from
    """

    DB_MODEL_CLASS = None
    SERIALIZER_CLASS = None

    def list(self, request):
        queryset = self.DB_MODEL_CLASS.objects.all()
        serializer = self.SERIALIZER_CLASS(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.DB_MODEL_CLASS.objects.all()
        db_object = get_object_or_404(queryset, pk=pk)
        serializer = self.SERIALIZER_CLASS(db_object)
        return Response(serializer.data)
