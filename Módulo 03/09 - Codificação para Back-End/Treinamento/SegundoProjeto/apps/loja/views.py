from django.shortcuts import render
from django.http import HttpResponse
from .models import Produtos

def saudacao(request):
    return HttpResponse("Olá mundo!!!")

def VerProdutos(request):
    produtos_lista = Produtos.objects.all()
    return render(request, 'index.html', {'produtos': produtos_lista})
def LinkInicial(request):
    return render(request, "index.html")
def LinkCadastro(request):
    return render(request, "cadastro.html")


