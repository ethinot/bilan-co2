from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django_app.models import User_data

admin.site.register(User_data)
