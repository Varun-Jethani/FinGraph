from django.db import models

# Create your models here.
class content(models.Model):
    stock = models.CharField(max_length=30)
    