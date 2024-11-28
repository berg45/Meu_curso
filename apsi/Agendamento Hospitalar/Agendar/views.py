from django.shortcuts import render, redirect
from .models import Visita
from .forms import VisitaForm
from django.contrib import messages

def listar_visitas(request):
    visitas = Visita.objects.all()
    return render(request, 'agenda/listar_visitas.html', {'visitas': visitas})


def agendar_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Visita agendada com sucesso!')
                return redirect('listar_visitas')
            except Exception as e:
                messages.error(request, str(e))
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = VisitaForm()
    return render(request, 'agenda/agendar_visita.html', {'form': form})

