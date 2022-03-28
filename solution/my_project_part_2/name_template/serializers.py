from name_template.models import Chocolate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ChocoTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chocolate
        fields = "__all__"

    def validate_name(self, name: str) -> str:
        if name.startswith("Choco"):
            return name
        raise ValidationError()
