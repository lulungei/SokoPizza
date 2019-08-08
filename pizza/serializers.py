from rest_framework import serializers
from . import models

class PizzasizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pizzasize
        fields = ('id', 'size', 'price')

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Toppings
        fields = ('id', 'name', 'small_price', 'medium_price', 'large_price', 'type')