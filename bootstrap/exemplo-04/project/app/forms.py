# forms.py
from django import forms
from .models import Usuario, Publicacao

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['name', 'email','nickname','senha','foto',]


class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['foto', 'titulo_prato', 'local', 'cidade', 'empresa']