from django.shortcuts import render
from .models import *

def VerHome(request):
    produtos_lista = Livros.objects.all()
    return render(request, "home.html", {'produtos': produtos_lista})

def VerProdutos(request):
    return render(request, "produtos.html", )
