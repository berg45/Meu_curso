from .models import Post

def post(request):
    postagens = Post.objects.first()
    return{
        'postagens': postagens
    }
