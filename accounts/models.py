import uuid
from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

from accounts.exceptions import InvalidPasswordCreationException
from currency.models import Currency

class Status(models.IntegerChoices):
    ACTIVE = 1, "Active"
    INACTIVE = 0, "Inactive"

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)
