from django.contrib import admin
from django.urls import path, include

# TODO здесь можно подключить urls Ваших приложений

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("choco.urls")),
    path("", include("get_list.urls")),
    path("", include("create_choco.urls")),
    path("", include("healthcheck.urls")),
    path("", include("name_template.urls"))
]
