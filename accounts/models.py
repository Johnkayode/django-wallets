from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager

import uuid


class CustomUser(AbstractUser):

    username = None
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email