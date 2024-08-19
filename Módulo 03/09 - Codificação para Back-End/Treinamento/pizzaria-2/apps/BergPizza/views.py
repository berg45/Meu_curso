from django.shortcuts import render, redirect
from .forms import FormularioCliente, FormularioPedido
from .models import Cliente, Pedido

def criar_cliente(request):
    if request.method == 'POST':
        form = FormularioCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = FormularioCliente()
    return render(request, 'clientes/formulario_cliente.html', {'form': form})

def criar_pedido(request):
    if request.method == 'POST':
        form = FormularioPedido(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = FormularioPedido()
    return render(request, 'pedidos/formulario_pedido.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})

