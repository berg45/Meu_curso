from django.shortcuts import render, redirect, get_object_or_404
from .models import Postagem, Comentario
from django.contrib.auth.decorators import login_required

def home(request):
    # Obtém todas as postagens ordenadas pela data mais recente
    postagens = Postagem.objects.all().order_by('-data')
    usuario = request.user
    
    # Se o usuário estiver autenticado, calcule seus likes e deslikes
    if usuario.is_authenticated:
        total_likes = usuario.likes.count()
        total_deslikes = usuario.deslikes.count()
    else:
        total_likes = total_deslikes = 0

    # Renderiza a página home com as postagens e informações do usuário
    return render(request, 'home.html', {
        'postagens': postagens,
        'usuario': usuario,
        'total_likes': total_likes,
        'total_deslikes': total_deslikes,
    })

@login_required
def toggle_like(request, post_id, action):
    """Função genérica para lidar com likes e deslikes."""
    postagem = get_object_or_404(Postagem, id=post_id)

    if action == 'like':
        if request.user in postagem.deslikes.all():
            postagem.deslikes.remove(request.user)  # Remove o deslike se ele já existir
        if request.user in postagem.likes.all():
            postagem.likes.remove(request.user)  # Remove o like se já tiver sido dado
        else:
            postagem.likes.add(request.user)  # Adiciona o like
    elif action == 'deslike':
        if request.user in postagem.likes.all():
            postagem.likes.remove(request.user)  # Remove o like se já existir
        if request.user in postagem.deslikes.all():
            postagem.deslikes.remove(request.user)  # Remove o deslike se já tiver sido dado
        else:
            postagem.deslikes.add(request.user)  # Adiciona o deslike

    # Redireciona de volta para a página de detalhes do post ou home
    return redirect('home')

@login_required
def like_post(request, post_id):
    """Gerencia a ação de dar like em uma postagem."""
    return toggle_like(request, post_id, 'like')

@login_required
def deslike_post(request, post_id):
    """Gerencia a ação de dar deslike em uma postagem."""
    return toggle_like(request, post_id, 'deslike')

@login_required
def comentar_post(request, post_id):
    """Adiciona um comentário a uma postagem."""
    if request.method == "POST":
        texto = request.POST.get('comentario')
        postagem = get_object_or_404(Postagem, id=post_id)
        Comentario.objects.create(usuario=request.user, postagem=postagem, texto=texto)
    return redirect('home')
