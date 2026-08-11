from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'city', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Perfil do blog', {'fields': ('age', 'city', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Perfil do blog', {'fields': ('email', 'age', 'city', 'profile_photo')}),
    )
    readonly_fields = ('created_at', 'updated_at', 'last_login', 'date_joined')
