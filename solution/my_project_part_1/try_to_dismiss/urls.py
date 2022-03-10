from try_to_dismiss.views import ResourceViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter


resource_router = SimpleRouter()
resource_router.register("resources", ResourceViewSet, basename='resource-viewset')

urlpatterns = [
    path("", include(resource_router.urls)),
]
