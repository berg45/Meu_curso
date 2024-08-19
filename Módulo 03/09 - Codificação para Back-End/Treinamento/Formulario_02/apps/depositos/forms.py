from django import forms
from .models import *

class FormularioProduto(forms.ModelForm):
    class Meta:
        model = Deposito
        fields = "__all__"

    