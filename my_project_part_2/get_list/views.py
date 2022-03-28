from rest_framework import viewsets
from get_list.models import Storage
from get_list.serializers import StorageSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


