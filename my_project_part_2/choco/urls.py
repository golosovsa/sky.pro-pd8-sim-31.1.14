from choco.views import ChocoViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter


vacation_router = SimpleRouter()
vacation_router.register("choco", ChocoViewSet, basename='vacation-viewset')

urlpatterns = [
    path("", include(vacation_router.urls)),
]
