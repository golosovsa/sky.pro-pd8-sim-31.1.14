from create_choco.views import ChocoCreateView
from django.urls import include, path
from rest_framework.routers import SimpleRouter


urlpatterns = [
    path("choco_create/", ChocoCreateView.as_view(), name="create-choco"),
]
