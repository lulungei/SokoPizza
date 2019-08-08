from rest_framework import routers, serializers, viewsets
from pizza import api_views as views


router = routers.DefaultRouter()
router.register(r'size', views.PizzasizeViewset)
router.register(r'toppings', views.ToppingsViewset)