from django.shortcuts import render, redirect
from .models import *
from .forms import *

def VerPacientes(request):
    lista_pacientes = Paciente.objects.all()
    return render(request, "index.html", {"pacientes": lista_pacientes})


def EditarPaciente(request, id_paciente):
    busca_paciente = Paciente.objects.get(id=id_paciente)
    if request.method == "POST":
        paciente_editado = FormularioPaciente(request.POST, instance=busca_paciente)
        if paciente_editado.is_valid():
            paciente_editado.save()
            return redirect('pagina_inicial')
    else:
        paciente_editado = FormularioPaciente()
    return render(request, "pagina-paciente.html", {"formulario": paciente_editado})

    