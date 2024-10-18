# app/forms.py

from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escreva seu comentário...'}),
        }

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'imagem']
