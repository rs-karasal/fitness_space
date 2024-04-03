from django.urls import path

from .views import ScheduleList, BookingList


urlpatterns = [
    path('', ScheduleList.as_view(), name='schedule-list'),
    path('bookings/', BookingList.as_view(), name='booking-list'),
]
