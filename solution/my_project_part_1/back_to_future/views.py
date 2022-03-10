from rest_framework import viewsets
from back_to_future.serializers import VacationSerializer
from back_to_future.models import Vacation


class VacationViewSet(viewsets.ModelViewSet):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
