from django.db import models
from django.conf import settings


class Trainer(models.Model):
    GYM_CHOICES = (
        ('gym1', 'Gym1'),
        ('gym2', 'Gym2'),
        ('gym3', 'Gym3'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="trainer_profile")
    full_name = models.CharField(max_length=255, verbose_name="Trainer full name")
    date_of_birth = models.DateField(verbose_name='Date of birth')
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female')), verbose_name='Gender')
    gyms = models.CharField(max_length=100, choices=GYM_CHOICES, verbose_name="Gym name", blank=True)
    specialization = models.CharField(max_length=255, verbose_name='Specialization', blank=True, null=True)
    description = models.TextField(verbose_name='Description', blank=True, null=True)

    def __str__(self):
        return self.full_name