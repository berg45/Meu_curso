from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import ComentarioForm

def lista_postagens(request):
    postagens = Post.objects.all().order_by('-data_criacao')
    return render(request, 'home.html', {'postagens': postagens})

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
