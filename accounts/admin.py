from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


class AdminUser(UserAdmin):
    list_display = ["email"]
    ordering = ["email"]


admin.site.register(User, AdminUser)
