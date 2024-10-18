# core/admin.py
from django.contrib import admin
from .models import Pizza, Order

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('sabor', 'tamanho', 'valor')
    list_filter = ('tamanho',)
    search_fields = ('sabor',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'pizza', 'quantidade', 'data_pedido')
    list_filter = ('data_pedido',)
    search_fields = ('pizza__sabor',)

