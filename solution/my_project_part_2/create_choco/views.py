from create_choco.models import Chocolate
from rest_framework import generics
from create_choco.serializers import ChocolateSerializer


class ChocoCreateView(generics.CreateAPIView):
    queryset = Chocolate.objects.all()
    serializer_class = ChocolateSerializer
