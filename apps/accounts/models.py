from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from apps.accounts.managers import CustomUserManager


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40,
                                blank=False,
                                null=False,
                                unique=True)
    is_manager = models.BooleanField(default=False)

    objects = CustomUserManager()

    class Meta:
        permissions = [("can_eat_pizzas", "Can eat pizzas")]

