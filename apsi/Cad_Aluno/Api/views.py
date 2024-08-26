from django.shortcuts import render, get_object_or_404,redirect
from .models import Aluno

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})

def detalhe_aluno(request, aluno_id):
    aluno = aluno = get_object_or_404(Aluno, pk=aluno_id)
    return render(request, 'detalhe_aluno.html', {'aluno': aluno})

def editar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    
    if request.method == 'POST':
        nome = request.POST.get('nome_aluno')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        aluno.nome = nome
        aluno.estado = estado
        aluno.cidade = cidade
        aluno.save()

        return redirect('detalhe_aluno', aluno_id=aluno.id)
    return render(request, 'editar_aluno.html', {'aluno': aluno})


def excluir_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'excluir_aluno.html', {'aluno': aluno})


def adicionar_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_aluno')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        
        print(f"Nome: {nome}, Estado: {estado}, Cidade: {cidade}")  # Depuração
        
        if nome and estado and cidade:
            aluno = Aluno(nome=nome, estado=estado, cidade=cidade)
            aluno.save()
            return redirect('lista_alunos')
        else:
           
            pass
    return render(request, 'adicionar_aluno.html')



    



