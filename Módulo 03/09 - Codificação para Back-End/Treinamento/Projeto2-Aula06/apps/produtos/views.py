from django.shortcuts import render
from .models import Produto

def inicial(request):
    produtos_lista = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos_lista})
#def inicial(request):
   # return render(request, "index.html")
def login(request):
    return render(request, "login.html")



