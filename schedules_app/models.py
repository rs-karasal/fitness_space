from django.db import models
from django.conf import settings

from trainers_app.models import Trainer


class Schedule(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="schedule_trainer", verbose_name="Trainer")
    gym = models.CharField(max_length=100, choices=Trainer.GYM_CHOICES, verbose_name="Gym")
    start_time = models.DateTimeField(verbose_name="Start time")
    end_time = models.DateTimeField(verbose_name="End time")
    
    def __str__(self):
        return f"{self.trainer.full_name} : {self.gym} : {self.start_time.strftime('%Y-%m-%d %H:%M')}"


class Booking(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="client_bookings", verbose_name="Booking client")
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="schedule_bookings", verbose_name="Booking schedule")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Booking time")
    
    def __str__(self):
        return f"{self.client.username} на {self.schedule}"
    