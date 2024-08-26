from django import forms
from .models import Pedidos, Clientes

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = '__all__'

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
