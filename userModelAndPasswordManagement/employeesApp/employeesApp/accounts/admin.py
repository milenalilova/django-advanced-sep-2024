from django.contrib import admin
from django.contrib.auth import get_user_model

from employeesApp.accounts.models import CustomUser

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    pass
