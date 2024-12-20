# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, Publicacao, Empresa
from .forms import UsuarioForm, PublicacaoForm # Assumindo que tens um formulário chamado UsuarioForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



def listar_usuarios(request):
    usuarios = Usuario.objects.all()  
    return render(request, 'usuario/listar_usuarios.html', {'usuarios': usuarios})


def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/criar_usuario.html', {'form': form})


def atualizar_usuario(request, aluno_id):
    usuario = get_object_or_404(Usuario, id=aluno_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario/atualizar_usuario.html', {'form': form, 'usuario': usuario})


def excluir_usuario(request, aluno_id):
    usuario = get_object_or_404(Usuario, id=aluno_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuario/excluir_usuario.html', {'usuario': usuario})


def detalhes_usuario(request, aluno_id):
    usuario = get_object_or_404(Usuario, id=aluno_id)
    return render(request, 'usuario/detalhes_usuario.html', {'usuario': usuario})

#crud para publicacao

def lista_publicacoes(request ):
    publicacoes = Publicacao.objects.all()
    return render(request, 'publicacoes/lista.html  ', {'publicacoes': publicacoes})


def criar_publicacao(request):
    if  request.method == 'POST':
        form = PublicacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_publicacoes')
    else :
        form = PublicacaoForm()
    return render(request, 'publicacoes/form.html',{'form': form})

def editar_publicacao(request, pk):
    publicacao = get_object_or_404(publicacao, pk=pk)
    if request.method == 'POST':
        form = PublicacaoForm(request.POST, request.FILES, instance=publicacao )
        if form.is_valid():
            form.save()
            return redirect('publicacoes')
    else:
        form =PublicacaoForm(instance=publicacao)

    return render(request, 'publicacoes/form.html',{'from':form})

def excluir_publicacao(request, pk):
    publicacao = get_object_or_404(Publicacao, pk=pk)
    if request.method == 'POST':
        publicacao.delete()
        return redirect('lista_publicacoes')
    return render(request, 'publicacoes/confimar_exclusao.html',{'publicacao':publicacao})

@login_required  # Garante que apenas usuários autenticados acessem
def TemplateView(request):
    publicacao = Publicacao.objects.filter(user=request.user).first()  # Obtenha a publicação do usuário atual
    empresas = ...  # Lógica para obter empresas
    
    context = {
        'user': request.user,
        'empresas': empresas,
        'publicacao': publicacao,
    }
    
    return render(request, 'dashboard.html', context)
    