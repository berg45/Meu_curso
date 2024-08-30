from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *
from .models import Produto
from .forms import ProdutoForm
from django.urls import reverse_lazy


class ProdutoListView(ListView):
    model = Produto
    template_name = 'admin/lista_produto.html'
    context_object_name = 'produtos'

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'Usuario/detalhes_produtos.html'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('lista_produto') #para gerar URLs
    template_name = 'admin/form_produto.html'

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('lista_produto')
    template_name = 'admin/form_produto.html'

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy('lista_produto')
    template_name = 'admin/confirmar_deletar_produto.html'
