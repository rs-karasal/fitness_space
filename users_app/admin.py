from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, AdminProfile


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_active', 'is_superuser']
    list_filter = ['role', 'is_active', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )


class AdminProfileAdmin(admin.ModelAdmin):
    model = AdminProfile
    list_display = ['user', 'description']
    list_filter = ['user']
    search_fields = ['user__username']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(AdminProfile, AdminProfileAdmin)