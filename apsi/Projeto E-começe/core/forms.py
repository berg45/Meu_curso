from django import forms

from.models import Produto, Clientes
from django.forms import ModelForm


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['img_produto','nome_produto', 'descricao', 'valorComDesconto', 'valorSemDesconto']
class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'cpf_cnpj', 'email', 'cep', 'endereco', 'numero', 'bairro', 'cidade', 'estado']

 
   