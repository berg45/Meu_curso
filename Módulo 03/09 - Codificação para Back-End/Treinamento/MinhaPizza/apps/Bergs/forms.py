from django import forms
from .models import Cliente, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'sabor', 'tamanho', 'pedido', 'preco']
