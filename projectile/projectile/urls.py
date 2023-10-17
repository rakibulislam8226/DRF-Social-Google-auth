from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    #
    path("auth/", include("drf_social_oauth2.urls")),
    path("social/", include("social_django.urls")),
]
