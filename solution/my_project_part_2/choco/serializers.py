from rest_framework import serializers
from choco.models import Chocolate


class ChocoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chocolate
        fields = "__all__"
