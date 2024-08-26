from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedidos, Clientes
from .forms import PedidosForm, ClientesForm

# CRUD para Pedidos
def pedidos_list(request):
    pedidos = Pedidos.objects.all()
    return render(request, 'pedidos_list.html', {'pedidos': pedidos})

def pedidos_create(request):
    if request.method == 'POST':
        form = PedidosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedidos_list')
    else:
        form = PedidosForm()
    return render(request, 'pedidos_form.html', {'form': form})

def pedidos_update(request, id):
    pedido = get_object_or_404(Pedidos, id=id)
    if request.method == 'POST':
        form = PedidosForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedidos_list')
    else:
        form = PedidosForm(instance=pedido)
    return render(request, 'pedidos_form.html', {'form': form})

def pedidos_delete(request, id):
    pedido = get_object_or_404(Pedidos, id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidos_list')
    return render(request, 'pedidos_confirm_delete.html', {'pedido': pedido})

# CRUD para Clientes
def clientes_list(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes_list.html', {'clientes': clientes})

def clientes_create(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')
    else:
        form = ClientesForm()
    return render(request, 'clientes_form.html', {'form': form})

def clientes_update(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')
    else:
        form = ClientesForm(instance=cliente)
    return render(request, 'clientes_form.html', {'form': form})

def clientes_delete(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes_list')
    return render(request, 'clientes_confirm_delete.html', {'cliente': cliente})


