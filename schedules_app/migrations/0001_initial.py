# Generated by Django 5.0.3 on 2024-04-03 11:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("trainers_app", "0002_alter_trainer_gender_alter_trainer_specialization"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gym",
                    models.CharField(
                        choices=[("gym1", "Gym1"), ("gym2", "Gym2"), ("gym3", "Gym3")],
                        max_length=100,
                        verbose_name="Gym",
                    ),
                ),
                ("start_time", models.DateTimeField(verbose_name="Start time")),
                ("end_time", models.DateTimeField(verbose_name="End time")),
                (
                    "trainer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedule_trainer",
                        to="trainers_app.trainer",
                        verbose_name="Trainer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Booking time"
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_bookings",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Booking client",
                    ),
                ),
                (
                    "schedule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedule_bookings",
                        to="schedules_app.schedule",
                        verbose_name="Booking schedule",
                    ),
                ),
            ],
        ),
    ]
