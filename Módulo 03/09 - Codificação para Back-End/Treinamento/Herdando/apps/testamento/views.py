from django.shortcuts import render

def VerIndex(request):
    return render(request, "index.html")

def VerLogin(request):
    return render(request, "login.html")

def VerProdutos(request):
    return render(request, "produtos.html")


