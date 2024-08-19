from django import forms
from.models import Clientes
from django.forms import ModelForm

class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ["name", "cpf_cnpj", "rg_ie", "zip_code", "address", "neighborhood", "number", "city", "state"]
    

 