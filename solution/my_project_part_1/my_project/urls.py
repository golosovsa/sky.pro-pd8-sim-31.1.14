from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

# TODO здесь можно подключить urls Ваших приложений

urlpatterns = [
    path("admin/", admin.site.urls),
    path("token/", views.obtain_auth_token),
    path("", include("smallest.urls")),
    path("", include("back_to_future.urls")),
    path("", include("comments_not_required.urls")),
    path("", include("try_to_dismiss.urls"))
]
