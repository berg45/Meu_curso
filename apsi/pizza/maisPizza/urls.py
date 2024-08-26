from django.urls import path
from .views import *

urlpatterns = [
    path("", ListaClientes, name="pagina_inicial"),
    path("clientes", criarCliente, name="criar_cliente"),
    path("pedido", criarPedido, name="criar_pedido"),
    
]