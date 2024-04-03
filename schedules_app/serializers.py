from rest_framework.serializers import ModelSerializer

from .models import Schedule, Booking


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"
        

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"