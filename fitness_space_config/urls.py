from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users_app.urls")),
    path("trainers/", include("trainers_app.urls")),
]
