from django.forms import ModelForm
from contextlib import nullcontext
from django.db import models
import uuid
# Create your models here.
class Trainee(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True, editable=False,serialize=True)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    age = models.PositiveBigIntegerField()
    field = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"