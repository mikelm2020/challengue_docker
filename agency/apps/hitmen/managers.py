#
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager, models.Manager):
    def _create_user(
        self, name, email, password, is_staff, is_superuser, is_active, **extra_fields
    ):
        user = self.model(
            name=name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, name, email, password=None, **extra_fields):
        return self._create_user(
            name, email, password, False, False, True, **extra_fields
        )

    def create_superuser(self, name, email, password=None, **extra_fields):
        return self._create_user(
            name, email, password, True, True, True, **extra_fields
        )

    def hitmen_in_system(self):
        return self.filter(is_superuser=False)

    def hitmen_by_manager(self, manager):
        return self.filter(manager=manager)

    def manager_of_hitman(self, hitman):
        return self.get(id=hitman).manager