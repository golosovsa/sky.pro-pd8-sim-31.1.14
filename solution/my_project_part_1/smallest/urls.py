from smallest.views import PostViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter


post_router = SimpleRouter()
post_router.register("smallest", PostViewSet, basename='smallest-posts')

urlpatterns = [
    path("", include(post_router.urls)),
]
