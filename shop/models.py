from django.db import models
from django.conf import settings

class Shop(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    address = models.CharField(max_length=50)

class Item(models.Model):
    shop = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)
    # photo
