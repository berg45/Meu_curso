from django.urls import path
from .import views

urlpatterns = [
    	path('', views.pizza_list, name='pizza_list'),
        path('pizza/<int:pk>/', views.pizza_detail, name='pizza_detail'),
        path('pizza/new/', views.pizza_create, name='pizza_create'),
        path('pizza/<int:pk>/edit/', views.pizza_edit, name='pizza_edit'),
        path('pizza/<int:pk>/delete/', views.pizza_delete, name='pizza_delete'),
        path('pedido/', views.criar_pedido, name='criar_pedido'),
        path('pedido/confirmado/', views.pedido_confirmado, name='pedido_confirmado'),
	]