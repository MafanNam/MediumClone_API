from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'id', 'user', 'gender', 'phone_number', 'country', 'city']
    list_display_links = ['pkid', 'id', 'user']
    list_filter = ['id', 'pkid']
