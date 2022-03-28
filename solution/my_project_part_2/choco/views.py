from rest_framework import viewsets
from choco.models import Chocolate
from choco.serializers import ChocoSerializer


class ChocoViewSet(viewsets.ModelViewSet):
    queryset = Chocolate.objects.all()[:5]
    serializer_class = ChocoSerializer
