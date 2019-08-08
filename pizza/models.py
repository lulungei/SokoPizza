from django.conf import settings
from django.db import models
from django.utils import timezone

class Pizzasize(models.Model):
    size = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=15)

class Toppings(models.Model):
    name = models.CharField(max_length=200)
    small_price = models.DecimalField(decimal_places=2, max_digits=15)
    medium_price = models.DecimalField(decimal_places=2, max_digits=15)
    large_price = models.DecimalField(decimal_places=2, max_digits=15)
    type = models.CharField(max_length=200)