from rest_framework import serializers
from create_choco.models import Chocolate


class ChocolateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chocolate
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "name": instance.name
        }
