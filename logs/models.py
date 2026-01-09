from django.db import models

# Create your models here.
class Log(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=128, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    message = models.TextField()

    def generate_code(self):
        return self.id