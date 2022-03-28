from name_template.views import CreateChocoTemplate
from django.urls import include, path
from rest_framework.routers import SimpleRouter


get_list_router = SimpleRouter()
get_list_router.register("chocolate/create/", CreateChocoTemplate, basename='template-viewset')

urlpatterns = [
    path("", include(get_list_router.urls)),
]
