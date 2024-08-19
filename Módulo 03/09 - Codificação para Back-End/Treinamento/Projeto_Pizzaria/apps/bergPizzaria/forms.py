from django import forms
from .models import Cliente, Pedido

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email']

class FormularioPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['descricao', 'data']