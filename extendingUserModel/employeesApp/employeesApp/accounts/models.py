from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from employeesApp.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )

    username = models.CharField(
        max_length=100,
        unique=True
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AppUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]


class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    profile_picture = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    age = models.IntegerField(
        null=True,
        blank=True
    )
