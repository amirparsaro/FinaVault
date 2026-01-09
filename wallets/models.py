from django.db import models
from django.utils import timezone

from currency.models import Currency
from accounts.models import User

class Status(models.IntegerChoices):
    ACTIVE = 1, "Active"
    INACTIVE = 0, "Inactive"

# Create your models here.
class Wallet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    wallet_code = models.CharField(max_length=128)
    balance = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)

    currency = models.OneToOneField(Currency, on_delete=models.CASCADE, null=True) # delete nullability later
    user = models.ForeignKey(User, on_delete=models.CASCADE)