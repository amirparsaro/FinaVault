from datetime import timezone
from django.db import models

from currency.models import Currency
from wallets.models import Wallet


# Create your models here.
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=128, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)

    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    payer = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='payer')
    payee = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='payee')