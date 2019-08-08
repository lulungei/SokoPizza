from django.urls import path
from . import views

urlpatterns=[
    path('make_order/', views.make_order, name='make_order'),
    path('handle_order', views.handle_order, name='handle_order'),
]