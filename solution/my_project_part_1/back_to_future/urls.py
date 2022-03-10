from back_to_future.views import VacationViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter


vacation_router = SimpleRouter()
vacation_router.register("back_to_future", VacationViewSet, basename='vacation-viewset')

urlpatterns = [
    path("", include(vacation_router.urls)),
]
