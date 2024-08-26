from django.urls import path
from .views import *

urlpatterns = [
    path("", ListaClientes, name="pagina_inicial"),
    path("clientes", criarCliente, name="pagina_cliente"),
    path("pedido", criarPedido, name="pagina_pedido"),
    
]