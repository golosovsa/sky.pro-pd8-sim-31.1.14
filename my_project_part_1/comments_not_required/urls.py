from comments_not_required.views import CalendarViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter


calendar_router = SimpleRouter()
calendar_router.register("events", CalendarViewSet, basename='events')

urlpatterns = [
    path("", include(calendar_router.urls)),
]
