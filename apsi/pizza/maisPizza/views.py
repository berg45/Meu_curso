from django.shortcuts import render, redirect
from .models import *
from .forms import *


def VerIndex(request):
    pedidos = Pedido.objects.all()
    return render(request, 'index.html', {'pedidos': pedidos})


def criarCliente(request):
    if request.method == 'POST':
        salvo_cliente = FormularioCliente(request.POST)
        if salvo_cliente.is_valid():
            salvo_cliente.save()
            return redirect('pagina_inicial')
    else:
        novo_cliente = FormularioCliente()
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'formulario': novo_cliente, 'clientes': clientes})

def criarPedido(request):
    if request.method == 'POST':
        salvo_pedido = FormularioPedido(request.POST)
        if salvo_pedido.is_valid():
            salvo_pedido.save()
            return redirect('pagina_inicial')
    else:
        novo_pedido = FormularioPedido()
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos.html', {'formulario': novo_pedido , 'pedidos': pedidos})
