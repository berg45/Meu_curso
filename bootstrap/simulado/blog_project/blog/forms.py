# blog/forms.py
from django import forms
from .models import Post, Comment, Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['name', 'email','nickname','senha','foto',]

class PostForm(forms.ModelForm):
    """Formulário para criação e edição de postagens."""
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título do post'
            }),
            'conteudo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Escreva o conteúdo aqui...'
            }),
        }

class ComentarioForm(forms.ModelForm):
    """Formulário para adicionar comentários."""
    class Meta:
        model = Comment
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Escreva um comentário...'
            }),
        }
