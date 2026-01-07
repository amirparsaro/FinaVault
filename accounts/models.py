from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from currency.models import Currency

class Status(models.IntegerChoices):
    ACTIVE = 1, "Active"
    INACTIVE = 0, "Inactive"

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128)
    account_code = models.CharField(max_length=128)
    balance = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)

    currency = models.OneToOneField(Currency, on_delete=models.CASCADE, null=True) # delete nullability later
    user = models.ForeignKey(User, on_delete=models.CASCADE)