from django.urls import path
from .views import *

urlpatterns = [
    path("", ListaClientes, name="pagina_inicial"),
    path("clientes", criarCliente, name="criar_cliente"),
    path("pedido", criarPedido, name="criar_pedido"),
    
      # Rotas para editar e excluir clientes
    path("clientes/editar/<int:id>/", editarCliente, name="editar_cliente"),
    path("clientes/excluir/<int:id>/", excluirCliente, name="excluir_cliente"),
    
    # Rotas para editar e excluir pedidos
    path("pedidos/editar/<int:id>/", editarPedido, name="editar_pedido"),
    path("pedidos/excluir/<int:id>/", excluirPedido, name="excluir_pedido"),
]
    
