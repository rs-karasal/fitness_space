from rest_framework.serializers import ModelSerializer

from .models import Trainer


class TrainerSerializer(ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"