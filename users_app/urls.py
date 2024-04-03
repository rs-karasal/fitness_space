from django.urls import path

from .views import CustomUserListCreateView, CustomUserDetailView


urlpatterns = [
    path("list/", CustomUserListCreateView.as_view(), name="customuser_list"),
    path("<int:pk>/", CustomUserDetailView.as_view(), name="customuser_detail"),
]