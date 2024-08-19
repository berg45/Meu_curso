from django.urls import path
from . import views

urlpatterns = [
    path('clientes/novo/', views.criar_cliente, name='criar_cliente'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('pedidos/novo/', views.criar_pedido, name='criar_pedido'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
]
