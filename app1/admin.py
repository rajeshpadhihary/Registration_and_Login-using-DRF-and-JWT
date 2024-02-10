from django.contrib import admin
from .models import customUser

@admin.register(customUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','first_name','first_name','is_active','is_staff','is_superuser')
    search_fields = ['username', 'email']