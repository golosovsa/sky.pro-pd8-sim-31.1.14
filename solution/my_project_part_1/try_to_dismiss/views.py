from rest_framework import viewsets
from try_to_dismiss.serializers import ResourceSerializer
from try_to_dismiss.models import Resource


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
