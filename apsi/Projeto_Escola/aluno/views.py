# aluno/views.py

from django.shortcuts import render
from core.models import Aluno  # Importa o modelo Aluno do app core

def area_aluno(request):
    alunos = Aluno.objects.all()  # Pega todos os alunos
    
    if request.method == 'POST':
        nome_aluno = request.POST.get('nome_aluno')
        try:
            aluno = Aluno.objects.get(nome=nome_aluno)
            turma = aluno.turma  # Acessando a turma do aluno
            disciplinas = turma.disciplinas.all()  # Acessando as disciplinas da turma
            professores = turma.professores.all()  # Acessando os professores da turma
            notas = aluno.nota_set.all()  # Notas do aluno
            return render(request, 'user_aluno/area_aluno.html', {
                'aluno_info': {
                    'aluno': aluno,
                    'turmas': [turma],  # Incluindo a turma do aluno
                    'disciplina': disciplinas,
                    'professores': professores,
                    'notas': notas
                }
            })
        except Aluno.DoesNotExist:
            return render(request, 'user_aluno/area_aluno.html', {'erro': 'Aluno não encontrado', 'alunos': alunos})
    
    # Se não for um POST, retorna todos os alunos
    return render(request, 'user_aluno/area_aluno.html', {'alunos': alunos})
