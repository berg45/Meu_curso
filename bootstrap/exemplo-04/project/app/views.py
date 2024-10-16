# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm  # Assumindo que tens um formulário chamado UsuarioForm
from django.http import HttpResponse


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
