from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

#
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    # STATUS
    ACTIVE = "A"
    INACTIVE = "I"
    #

    STATUS_CHOICES = [
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive"),
    ]

    name = models.CharField("Name", max_length=30)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    description = models.TextField("Description", max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="A")
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="manager_of",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name"]

    objects = UserManager()
