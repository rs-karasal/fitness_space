from rest_framework import generics

from .models import Schedule, Booking
from .serializers import ScheduleSerializer, BookingSerializer


class ScheduleList(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    

class BookingList(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
