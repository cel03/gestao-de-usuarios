from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager

import datetime


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Endereço de email'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField(default=datetime.date.today)
    name = models.CharField(max_length=50)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
      verbose_name = 'usuário'
      verbose_name_plural = 'usuários'


    def __str__(self):
        return self.email
    