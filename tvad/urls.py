from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # создание клиента
    path('create_customer', views.create_customer, name='create_customer'),
    path('customer', views.customer, name='customer'),
    path('advertisement', views.advertisement, name='advertisement'),
    path('broadcast', views.broadcast, name='broadcast'),
    path('rating', views.rating, name='rating'),
]