from django.db import models
from accounts.models import User


# Create your models here.
class Log(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=128, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    message = models.TextField()

    user = models.ManyToManyField(User)

    def generate_code(self):
        return self.id