from django.urls import path, include
from .views import *

urlpatterns = [
    path('', catalog, name='catalog'),
    path('contacts', contacts, name='contacts'),
    path('conditions', conditions, name='conditions'),
    path(f'cart', usercart, name='usercart'),
    path(f'order/<int:pk>', order, name='order'),
    path(f'<slug:slug>', products, name='products'),
    path(f'<slug:slug>/<int:pk>', single_product, name='single-product'),


]