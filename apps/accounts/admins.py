from django.contrib import admin

from .models import CustomUser

class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'npm', 'date_joined', 'last_login']