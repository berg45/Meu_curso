# app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comentario
from .forms import ComentarioForm
from django.contrib.auth.decorators import login_required

@login_required  # Essa decorator exige que o usuário esteja logado
def dashboard(request):
    total_postagens = Post.objects.count()
    ultimas_postagens = Post.objects.order_by('-data_criacao')[:6]  # Últimas 6 postagens

    user_info = {
        'username': request.user.username,
        'profile_picture': request.user.profile.profile_picture.url if hasattr(request.user, 'profile') else None
    }

    return render(request, 'dashboard.html', {
        'total_postagens': total_postagens,
        'ultimas_postagens': ultimas_postagens,
        'user_info': user_info,
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


