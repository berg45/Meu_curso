from django import forms
from django.contrib.auth.models import User
from.models import Produto, Clientes
from django.forms import ModelForm


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['img_produto','nome_produto', 'descricao', 'valorComDesconto', 'valorSemDesconto']
class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ["nome", "cpf_cnpj", "cep", "endereço", "bairro", "numero", "cidade", "estado"]