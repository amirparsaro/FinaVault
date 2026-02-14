from django.db import models
from django.utils import timezone

from currency.models import Currency
from accounts.models import User

class Status(models.IntegerChoices):
    ACTIVE = 1, "Active"
    INACTIVE = 0, "Inactive"

class Type(models.IntegerChoices):
    SAVING = 0, "Saving"
    CHECKING = 1, "Checking",

# Create your models here.
class Wallet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    wallet_code = models.CharField(max_length=128, unique=True)
    balance = models.DecimalField(max_digits=18, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)
    account_type = models.IntegerField(choices=Type.choices, default=Type.SAVING)

    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True) # delete nullability later
    user = models.ForeignKey(User, on_delete=models.CASCADE)