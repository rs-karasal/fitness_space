from django.urls import path

from .views import TrainerListView, TrainerDetailView


urlpatterns = [
    path("list/", TrainerListView.as_view(), name="trainers_list"),
    path("<int:pk>/", TrainerDetailView.as_view(), name="trainers_detail"),
]