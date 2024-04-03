from rest_framework import generics

from .models import Trainer
from .serializers import TrainerSerializer


class TrainerListView(generics.ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    

class TrainerDetailView(generics.RetrieveAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
