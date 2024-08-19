from django import forms
from .models import *

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class FormularioPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = "__all__"
