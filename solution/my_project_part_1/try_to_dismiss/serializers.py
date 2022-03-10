from dateutil.utils import today
from rest_framework import serializers

from try_to_dismiss.models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    is_active = serializers.ReadOnlyField()
    dismiss_date = serializers.DateField()

    def validate_dismiss_date(self, date):
        if date < today().date():
            raise serializers.ValidationError("Incorrect dismiss date")
        return date

    class Meta:
        model = Resource
        fields = "__all__"
