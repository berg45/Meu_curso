from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, Publicacao, Empresa
from app.forms import UsuarioForm, PublicacaoForm # Assumindo que tens um formulário chamado UsuarioForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def lista_publicacoes(request ):
    publicacoes = Publicacao.objects.all()
    return render(request, 'lista.html ', {'publicacoes': publicacoes})


def criar_publicacao(request):
    if  request.method == 'POST':
        form = PublicacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_publicacoes')
    else :
        form = PublicacaoForm()
    return render(request, 'form.html',{'form': form})

def editar_publicacao(request, pk):
    publicacao = get_object_or_404(Publicacao, pk=pk)
    if request.method == 'POST':
        form = PublicacaoForm(request.POST, request.FILES, instance=publicacao )
        if form.is_valid():
            form.save()
            return redirect('lista_publicacoes')
    else:
        form =PublicacaoForm(instance=publicacao)
   
    return render(request, 'form.html',{'form':form})

def excluir_publicacao(request, pk):
    publicacao = get_object_or_404(Publicacao, pk=pk)
    if request.method == 'POST':
        publicacao.delete()
        return redirect('lista_publicacoes')
    return render(request, 'confirmar_exclusao.html',{'publicacao':publicacao})