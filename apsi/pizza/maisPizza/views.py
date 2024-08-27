from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def ListaClientes(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})


def criarCliente(request):
    if request.method == 'POST':
        salvo_cliente = FormularioCliente(request.POST)
        if salvo_cliente.is_valid():
            salvo_cliente.save()
            return redirect('pagina_inicial')
    else:
        novo_cliente = FormularioCliente()
    clientes = Cliente.objects.all()
    return render(request, 'criar_clientes.html', {'formulario': novo_cliente, 'clientes': clientes})

def editarCliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = FormularioCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('pagina_inicial')
    else:
        form = FormularioCliente(instance=cliente)
    return render(request, 'editar_cliente.html', {'formulario': form})

def excluirCliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('pagina_inicial')
    return render(request, 'excluir_cliente.html', {'cliente': cliente})

def criarPedido(request):
    if request.method == 'POST':
        salvo_pedido = FormularioPedido(request.POST)
        if salvo_pedido.is_valid():
            salvo_pedido.save()
            return redirect('pagina_inicial')
    else:
        novo_pedido = FormularioPedido()
    pedidos = Pedido.objects.all()
    return render(request, 'criar_pedidos.html', {'formulario': novo_pedido , 'pedidos': pedidos})
# View para editar pedido
def editarPedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        form = FormularioPedido(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pagina_inicial')
    else:
        form = FormularioPedido(instance=pedido)
    return render(request, 'editar_pedido.html', {'formulario': form})

# View para excluir pedido
def excluirPedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pagina_inicial')
    return render(request, 'excluir_pedido.html', {'pedido': pedido})

