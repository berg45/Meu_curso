from django.shortcuts import render, get_object_or_404,redirect
from .models import Aluno
from .forms import AlunoForm

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
        foto = request.FILES.get('foto')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')

        aluno.nome = nome
        aluno.foto = foto
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
        foto = request.FILES.get('foto')  # Obtendo o arquivo enviado
        
       
        print(f"Nome: {nome}, Foto: {foto}, Estado: {estado}, Cidade: {cidade}")
        
        if nome and estado and cidade and foto:
            aluno = Aluno(nome=nome, foto=foto, estado=estado, cidade=cidade)
            aluno.save()
            return redirect('lista_alunos')
        else:
            
            print("Dados do formulário incompletos ou foto não enviada.")  # Depuração

    return render(request, 'adicionar_aluno.html')




    



