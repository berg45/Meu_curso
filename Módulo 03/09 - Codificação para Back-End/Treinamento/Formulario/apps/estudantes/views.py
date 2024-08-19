from django.shortcuts import render, redirect
from .models import *
from .forms import *

def CriarEstudante(request):
    busca_estudantes = Estudante.objects.all()
    if request.method == "POST":
        novo_estudante = FormularioEstudante(request.POST)
        if novo_estudante.is_valid():
            novo_estudante.save()
            return redirect("pagina_estudantes")
    else:
        novo_estudante = FormularioEstudante()
    return render(request, "pagina_estudantes.html", {"formulario": novo_estudante, "estudantes": busca_estudantes})    




