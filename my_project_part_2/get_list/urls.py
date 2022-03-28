from choco.views import ChocoViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter


get_list_router = SimpleRouter()
get_list_router.register("get_list", ChocoViewSet, basename='vacation-viewset')

urlpatterns = [
    path("", include(get_list_router.urls)),
]
