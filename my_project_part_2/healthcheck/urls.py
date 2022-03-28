from healthcheck.views import ReadyCheckView, LifeCheckView, HealthCheckView
from django.urls import include, path
from rest_framework.routers import SimpleRouter


urlpatterns = [
    path("healthcheck/", HealthCheckView.as_view(), name="healthcheck"),
    path("lifecheck/", LifeCheckView.as_view(), name="lifecheck"),
    path("readycheck/", ReadyCheckView.as_view(), name="readycheck")
]

