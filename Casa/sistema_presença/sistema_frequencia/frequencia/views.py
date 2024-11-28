from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno, Turma, Presenca
from django.utils import timezone

def marcar_presenca(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    hoje = timezone.now().date()
    presenca, created = Presenca.objects.get_or_create(aluno=aluno, data=hoje)
    presenca.presente = not presenca.presente  # Alterna entre presente/ausente
    presenca.save()
    return redirect('frequencia:detalhe_aluno', aluno_id=aluno.id)

def detalhe_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    presencas = Presenca.objects.filter(aluno=aluno).order_by('-data')
    return render(request, 'frequencia/detalhe_aluno.html', {'aluno': aluno, 'presencas': presencas})

def lista_alunos(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    alunos = turma.alunos.all()
    return render(request, 'frequencia/lista_alunos.html', {'turma': turma, 'alunos': alunos})

