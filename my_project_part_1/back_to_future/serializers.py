from rest_framework import serializers
from back_to_future.models import Vacation


class VacationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacation
        fields = ("user", "date_from", "date_to", "code")
