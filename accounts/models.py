from django.db import models
from django.contrib.auth.hashers import make_password, check_password

from accounts.exceptions import InvalidPasswordCreationException
from currency.models import Currency

class Status(models.IntegerChoices):
    ACTIVE = 1, "Active"
    INACTIVE = 0, "Inactive"

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128) # TODO: Unique = True!!!
    password = models.CharField(max_length=128)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)

    def set_password(self, raw_password: str):
        if len(raw_password) < 8:
            raise InvalidPasswordCreationException("Password must be at least 8 characters long.")

        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
