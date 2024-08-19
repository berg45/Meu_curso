from django.shortcuts import render
from .models import *

def VerInicial(request):
    lista = Movel.objects.all()
    return render(request, "inicial.html", {"inicial": lista})

def VerCadastro(request):
    lista = Cadastro.objects.all()
    return render(request, "cadastro.html", {"pessoas": lista})