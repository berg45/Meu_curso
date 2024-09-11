from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno, Professor, Turma, Disciplina, Nota
from .forms import AlunoForm, ProfessorForm, TurmaForm, DisciplinaForm, NotaForm

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/listar_alunos.html', {'alunos': alunos})

def detalhes_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    notas = Nota.objects.filter(aluno=aluno).select_related('disciplina__professor')
    return render(request, 'alunos/detalhes_aluno.html', {'aluno': aluno, 'notas': notas})


def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
    return render(request, 'alunos/form_aluno.html', {'form': form})

def atualizar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'alunos/form_aluno.html', {'form': form})

def excluir_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('listar_alunos')
    return render(request, 'alunos/confirmar_exclusao.html', {'aluno': aluno})

#professores
def listar_professores(request):
    professores = Professor.objects.all()
    return render(request, 'professores/listar_professores.html', {'professores': professores})

def criar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_professores')
    else:
        form = ProfessorForm()
    return render(request, 'professores/criar_professor.html', {'form': form})

def atualizar_professor(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('listar_professores')
    else:
        form = ProfessorForm(instance=professor)
    return render(request, 'professores/atualizar_professor.html', {'form': form})

def excluir_professor(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    if request.method == 'POST':
        professor.delete()
        return redirect('listar_professores')
    return render(request, 'professores/excluir_professor.html', {'professor': professor})

def detalhes_professor(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    return render(request, 'professores/detalhes_professor.html', {'professor': professor})

# Turma views
def listar_turmas(request):
    turmas = Turma.objects.all()
    return render(request, 'turmas/listar_turmas.html', {'turmas': turmas})

def criar_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_turmas')
    else:
        form = TurmaForm()
    return render(request, 'turmas/criar_turma.html', {'form': form})

def atualizar_turma(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            return redirect('listar_turmas')
    else:
        form = TurmaForm(instance=turma)
    return render(request, 'turmas/atualizar_turma.html', {'form': form})

def excluir_turma(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    if request.method == 'POST':
        turma.delete()
        return redirect('listar_turmas')
    return render(request, 'turmas/excluir_turma.html', {'turma': turma})

def detalhes_turma(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    return render(request, 'turmas/detalhes_turma.html', {'turma': turma})

# Disciplina views
def listar_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'disciplinas/listar_disciplinas.html', {'disciplinas': disciplinas})

def criar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_disciplinas')
    else:
        form = DisciplinaForm()
    return render(request, 'disciplinas/criar_disciplina.html', {'form': form})

def atualizar_disciplina(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('listar_disciplinas')
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'disciplinas/atualizar_disciplina.html', {'form': form})

def excluir_disciplina(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    if request.method == 'POST':
        disciplina.delete()
        return redirect('listar_disciplinas')
    return render(request, 'disciplinas/excluir_disciplina.html', {'disciplina': disciplina})

def detalhes_disciplina(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    return render(request, 'disciplinas/detalhes_disciplina.html', {'disciplina': disciplina})

# Nota views
def listar_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/listar_notas.html', {'notas': notas})

def criar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_notas')
    else:
        form = NotaForm()
    return render(request, 'notas/criar_nota.html', {'form': form})

def atualizar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('listar_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas/atualizar_nota.html', {'form': form})

def excluir_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('listar_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas/excluir_nota.html', {'from': form})