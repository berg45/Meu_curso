from django.shortcuts import render, redirect
from .models import *
from .forms import *

def VerDeposito(request):
    buscar_depositos = Deposito.objects.all()
    if request.method == "POST":
        novo_produto = FormularioProduto(request.POST)
        if novo_produto.is_valid():
            novo_produto.save()
            return redirect('pagina_deposito')
    else:
        novo_produto = FormularioProduto()
        return render(request, 'pagina_deposito.html', {'formulario': novo_produto, 'depositos': buscar_depositos})    

