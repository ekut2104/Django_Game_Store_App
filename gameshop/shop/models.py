from django.db import models


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=False)
    price = models.FloatField(null=False, blank=False, unique=False)
