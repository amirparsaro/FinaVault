from django.db import models

# Create your models here.
class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=128, unique=True)
    symbol = models.CharField(max_length=10, unique=True)
    exchange_rate = models.FloatField()

    base_currency = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)