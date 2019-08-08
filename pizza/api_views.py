from rest_framework import viewsets
from . import models
from . import serializers

class PizzasizeViewset(viewsets.ModelViewSet):
    queryset = models.Pizzasize.objects.all()
    serializer_class = serializers.PizzasizeSerializer

class ToppingsViewset(viewsets.ModelViewSet):
    queryset = models.Toppings.objects.all()
    serializer_class = serializers.ToppingSerializer