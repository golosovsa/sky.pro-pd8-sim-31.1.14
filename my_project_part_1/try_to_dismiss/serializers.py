from rest_framework import serializers

from try_to_dismiss.models import Resource


# TODO добавьте необходимый код в сериалайзер ниже
class ResourceSerializer(serializers.ModelSerializer):
    is_active = serializers.ReadOnlyField()
    dismiss_date = serializers.DateField()

    class Meta:
        model = Resource
        fields = "__all__"
