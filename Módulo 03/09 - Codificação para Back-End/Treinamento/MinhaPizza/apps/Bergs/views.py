from django.shortcuts import render, redirect
from .models import Cliente, Pedido
from .forms import ClienteForm, PedidoForm

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def add_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'add_cliente.html', {'form': form})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})

def add_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'add_pedido.html', {'form': form})

