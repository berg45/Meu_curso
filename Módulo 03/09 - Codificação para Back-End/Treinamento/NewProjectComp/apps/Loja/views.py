from django.shortcuts import render
from .models import produto

def VerProdutos(request):
    produtos_lista = produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos_lista})


def LinkCadastro(request):
    return render(request, 'login.html')
 

