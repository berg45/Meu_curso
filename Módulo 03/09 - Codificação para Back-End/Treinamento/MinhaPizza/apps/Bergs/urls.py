from django.urls import path
from .views import *

urlpatterns = [
    path('', lista_clientes, name='lista_clientes'),
    path('add_cliente/', add_cliente, name='add_cliente'),
    path('pedidos/', lista_pedidos, name='lista_pedidos'),
    path('add_pedido/', add_pedido, name='add_pedido'),
]
