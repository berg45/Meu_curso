from django.urls import path
from .views import *

urlpatterns = [
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/novo/', criar_cliente, name='criar_cliente'),
    path('pedidos/', lista_pedidos, name='lista_pedidos'),
    path('pedidos/novo/', criar_pedido, name='criar_pedido'),
]
