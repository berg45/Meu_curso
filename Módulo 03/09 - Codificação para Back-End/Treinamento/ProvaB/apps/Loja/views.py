from django.shortcuts import render
from .models import *

def VerProdutos(request):
    produtos_lista = Produto.objects.all()
    return render(request, 'home.html', {'produtos': produtos_lista})

def LinkInicial(request):
    produtos_lista = Produto.objects.all()
    return render(request, 'pg_inicial.html', {'produtos': produtos_lista})

def LinkCadastro(request):
    produtos_lista = Cadastro.objects.all()
    return render(request, 'cadastro.html', {'produtos': produtos_lista})

def LinkLogin(request):
    produtos_lista = Login.objects.all()
    return render(request, 'login.html', {'produtos': produtos_lista})