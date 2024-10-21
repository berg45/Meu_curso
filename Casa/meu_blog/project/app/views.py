# app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy    
from .models import Post, Comentario
from .forms import ComentarioForm, PostForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    total_postagens = Post.objects.count()
    ultimas_postagens = Post.objects.all().order_by('-data_criacao')[:6]  # Exibe as 6 postagens mais recentes

    # Verifica se o usuário tem um perfil com foto
    profile_picture = None
    if hasattr(request.user, 'profile') and request.user.profile.profile_picture:
        profile_picture = request.user.profile.profile_picture.url

    return render(request, 'dashboard.html', {
        'total_postagens': total_postagens,
        'ultimas_postagens': ultimas_postagens,
        'profile_picture': profile_picture,  # Passa a foto de perfil se existir
    })




# app/views.py

def lista_postagens(request):
    postagens = Post.objects.all().order_by('-data_criacao')
    return render(request, 'lista_postagens.html', {'postagens': postagens})

def detalhes_postagem(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comentarios.all()
    
    if request.method == 'POST':
        if 'curtir' in request.POST:
            post.curtidas += 1
            post.save()
            return redirect('detalhes_postagem', post_id=post.id)
        else:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.post = post
                comentario.usuario = request.user
                comentario.save()
                return redirect('detalhes_postagem', post_id=post.id)
    else:
        form = ComentarioForm()

    return render(request, 'detalhes_postagem.html', {'post': post, 'comentarios': comentarios, 'form': form})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_postagens')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('lista_postagens')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_postagens')
    return render(request, 'post_confirm_delete.html', {'post': post})


