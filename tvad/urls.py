from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # создание клиента
    path('create_customer', views.create_customer, name='create_customer'),
    path('customer', views.customer, name='customer'),
    path('updateStatusAdv', views.updateStatusAdv, name='updateStatusAdv'),
    path('create_advertisement', views.create_advertisement, name='create_advertisement'),
    path('advertisement', views.advertisement, name='advertisement'),
    path('create_broadcast', views.create_broadcast, name='create_broadcast'),
    path('broadcast', views.broadcast, name='broadcast'),
    path('broadcast/<int:id>', views.broadcast_view, name='broadcast_view'),
    path('create_rating', views.create_rating, name='create_rating'),
    path('rating', views.rating, name='rating'),
    path('search_cal', views.search_cal, name='search_cal'),
    path('clear_session', views.clear_session, name='clear_session'),
    path('calculate_cost', views.calculate_cost, name='calculate_cost'),
    path('calculation', views.calculation, name='calculation'),
]