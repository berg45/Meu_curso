from django.shortcuts import render, redirect
from .models import *
from .forms import *

def CriarHamburguer(request):
    busca_pedidos = Hamburguer.objects.all()
    if request.method == "POST":
        novo_pedido = FormularioPedido(request.POST)
        if novo_pedido.is_valid():
            novo_pedido.save()
            return redirect("pagina_inicial")
    else:
        novo_pedido =  FormularioPedido()
        return render(request, "pedidos.html", {"formulario": novo_pedido, "Burguer": busca_pedidos})
