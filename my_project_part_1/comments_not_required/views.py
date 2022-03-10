from rest_framework import viewsets
from comments_not_required.serializers import CalendarEventsSerializer
from comments_not_required.models import Calendar


class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarEventsSerializer
