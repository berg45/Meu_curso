from django import forms
from .models import *

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'cep', 'endereco', 'bairro']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
        }

    
class FormularioPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = "__all__"