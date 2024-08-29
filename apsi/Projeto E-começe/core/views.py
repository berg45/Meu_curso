from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoForm
from django.urls import reverse_lazy

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/lista_produto.html'

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produtos/detalhes_produtos.html'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('lista_produto')
    template_name = 'produtos/form_produto.html'

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('lista_produto')
    template_name = 'produtos/form_produto.html'

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy('lista_produto')
    template_name = 'produtos/confirmar_deletar_produto.html'
