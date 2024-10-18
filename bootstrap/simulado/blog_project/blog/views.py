# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Interaction
from .forms import PostForm, ComentarioForm

def index(request):
    posts = Post.objects.all().order_by('-data_criacao')
    return render(request, 'index.html', {'posts': posts})


def add_post(request):
    """Cria uma nova postagem."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user  # Atribui o autor ao usuário logado
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

@login_required
def add_comment(request, post_id):
    """Adiciona um comentário a uma postagem específica."""
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            return redirect('post_comments', post_id=post.id)
    else:
        form = ComentarioForm()
    return render(request, 'blog/post_comments.html', {
        'post': post,
        'form': form,
        'comentarios': post.comentarios.all()
    })

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    interaction, created = Interaction.objects.get_or_create(post=post, user=request.user, defaults={'tipo_interacao': 'like'})
    
    if not created:
        if interaction.tipo_interacao == 'like':
            interaction.delete()  # Remove like
            post.likes -= 1
        else:
            interaction.tipo_interacao = 'like'
            post.likes += 1
            post.deslikes -= 1
        post.save()
    else:
        post.likes += 1
        post.save()

    return JsonResponse({'likes': post.likes, 'deslikes': post.deslikes})

@login_required
def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    interaction, created = Interaction.objects.get_or_create(post=post, user=request.user, defaults={'tipo_interacao': 'dislike'})

    if not created:
        if interaction.tipo_interacao == 'dislike':
            interaction.delete()  # Remove dislike
            post.deslikes -= 1
        else:
            interaction.tipo_interacao = 'dislike'
            post.deslikes += 1
            post.likes -= 1
        post.save()
    else:
        post.deslikes += 1
        post.save()

    return JsonResponse({'likes': post.likes, 'deslikes': post.deslikes})




