from name_template.views import CreateChocoTemplate
from django.urls import path


urlpatterns = [
    path("chocolate/create/", CreateChocoTemplate.as_view(), name='template-view'),
]
