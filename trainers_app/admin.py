from django.contrib import admin

from .models import Trainer

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ["full_name", "gender", "specialization",]
    list_filter = ["gender", "gyms",]
    search_fields = ["full_name", "specialization",]