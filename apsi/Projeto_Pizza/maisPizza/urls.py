from django.urls import path
from . import views

urlpatterns = [
    # Rotas para Pedidos
    path('', views.pedidos_list, name='pedidos_list'),
    path('pedidos/create/', views.pedidos_create, name='pedidos_create'),
    path('pedidos/update/<int:id>/', views.pedidos_update, name='pedidos_update'),
    path('pedidos/delete/<int:id>/', views.pedidos_delete, name='pedidos_delete'),
    
    # Rotas para Clientes
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('clientes/create/', views.clientes_create, name='clientes_create'),
    path('clientes/update/<int:id>/', views.clientes_update, name='clientes_update'),
    path('clientes/delete/<int:id>/', views.clientes_delete, name='clientes_delete'),
]
