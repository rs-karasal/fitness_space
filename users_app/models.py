from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("client", "Client"),
        ("trainer", "Trainer"),
        ("admin", "Admin"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="client", verbose_name="role")


class AdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="admin_profile")
    description = models.TextField(verbose_name="About admin", blank=True)

    def __str__(self):
        return f"Администратор {self.user.username}"

    
@receiver(post_save, sender=CustomUser)
def create_or_update_admin_profile(sender, instance, created, **kwargs):
    if instance.role == 'admin' and not instance.is_superuser:
        instance.is_superuser = True
        instance.save(update_fields=['is_superuser'])
        AdminProfile.objects.get_or_create(user=instance)
    elif hasattr(instance, 'admin_profile') and instance.role != 'admin':
        instance.admin_profile.delete()