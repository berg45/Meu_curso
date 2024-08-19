from django.shortcuts import render
from .models import Produto

def VerProdutos(request):
    produtos_lista = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos_lista})

def LinkInicial(request):
    produtos_listas = Produto.objects.all()
    return render(request, "index.html", {'produtos': produtos_listas})

def LinkCadastro(request):
    cadastro = Produto.objects.all()
    return render(request, "cadastro.html")