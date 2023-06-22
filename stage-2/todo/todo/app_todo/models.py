from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)
