from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Pizza, Order
from .forms import PizzaForm, OrderForm

def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizza_list.html', {'pizzas': pizzas})

def pizza_detail(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    return render(request, 'pizza_detail.html',{'pizza': pizza})

#cria uma nova pizza
def pizza_create(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pizza_list')
    else:
        form = PizzaForm()
    return render(request,  'pizza_form.html', {'form': form})

# Editar uma pizza existente
def pizza_edit(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect('pizza_list')
    else:
        form = PizzaForm(instance=pizza)
    return render(request, 'pizza_form.html', {'form': form})

def pizza_delete(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    if request.method == 'POST':
        pizza.delete()
        return redirect('pizza_list')
    return render(request, 'pizza_confirm_delete.html', {'pizza': pizza})



def criar_pedido(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            pedidos_realizados = []
            for field_name, quantidade in form.cleaned_data.items():
                if quantidade and quantidade > 0:
                    try:
                        # Extrair o ID da pizza a partir do nome do campo
                        pizza_id = int(field_name.split('_')[1])
                        pizza = Pizza.objects.get(id=pizza_id)
                        Order.objects.create(pizza=pizza, quantidade=quantidade)
                        pedidos_realizados.append(f"{pizza.get_tamanho_display()} {pizza.sabor} x {quantidade}")
                    except (IndexError, ValueError, Pizza.DoesNotExist):
                        # Ignorar campos com nomes inválidos ou pizzas inexistentes
                        continue
            if pedidos_realizados:
                messages.success(request, f"Pedido confirmado: {', '.join(pedidos_realizados)}")
                return redirect('pedido_confirmado')
            else:
                messages.warning(request, "Nenhuma pizza foi selecionada para o pedido.")
    else:
        form = OrderForm()
    pizzas = Pizza.objects.all()
    return render(request, 'criar_pedido.html', {'form': form, 'pizzas': pizzas})

def pedido_confirmado(request):
    return render(request, 'pedido_confirmado.html')