from django import forms
from .models import *

class FormularioPedido(forms.ModelForm):
    class Meta:
        model = Hamburguer
        fields = "__all__"