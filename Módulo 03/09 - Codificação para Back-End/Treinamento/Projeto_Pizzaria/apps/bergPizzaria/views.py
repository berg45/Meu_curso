from django.shortcuts import render, redirect
from .models import *
from .forms import *

def criar_cliente(request):
    if request.method == 'GET' and 'nome' in request.GET:
        novo_cliente = FormularioCliente(request.GET)
        if salvo_cliente.is_valid():
            salvo_cliente.save()
            return redirect('lista_clientes')
    else:
        salvo_cliente = FormularioCliente()
    return render(request, 'formulario_clientes.html', {'form': novo_cliente})

def criar_pedido(request):
    if request.method == 'GET' and 'descricao' in request.GET:
        novo_pedido = FormularioPedido(request.GET)
        if pedido_salvo.is_valid():
            pedido_salvo.save()
            return redirect('lista_pedidos')
    else:
        pedido_salvo = FormularioPedido()
    return render(request, 'formulario_pedidos.html', {'form': novo_pedido})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente.html', {'clientes': clientes})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos.html', {'pedidos': pedidos})



