from rest_framework import serializers
from comments_not_required.models import Calendar


class CalendarEventsSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(
        max_length=200,
        read_only=True,
        allow_null=True,
        allow_blank=True,
    )

    class Meta:
        model = Calendar
        fields = "__all__"

