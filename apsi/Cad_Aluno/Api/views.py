from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno


def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})

def detalhe_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    return render(request, 'detalhe_aluno.html', {'aluno': aluno})

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



