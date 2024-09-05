from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *
from .models import Produto, Clientes
from .forms import ProdutoForm, ClientesForm
from django.urls import reverse_lazy


class ProdutoListView(ListView):
    model = Produto
    template_name = 'admin/lista_produtos.html'
    context_object_name = 'produtos'

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'admin/detalhes_produtos.html'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('lista_produtos') #para gerar URLs
    template_name = 'admin/form_produto.html'

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('lista_produtos')
    template_name = 'admin/form_produto.html'

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy('lista_produtos')
    template_name = 'admin/confirmar_deletar_produto.html'

#Formulario clientes.......

def cliente_list(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes/clientes_list.html', {'clientes': clientes})

def cliente_detail(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})

def cliente_create(request):
    if request.method == "POST":
        form = ClientesForm(request.POST)
        if form.is_valid():
            print("Formulário válido. Salvando...")
            cliente = form.save()
            print("Formulário salvo com sucesso. Cliente:", cliente)
            return redirect('cliente_list')
        else:
            print("Formulário inválido. Erros:", form.errors)
    else:
        form = ClientesForm()

    return render(request, 'clientes/cliente_form.html', {'form': form})

def cliente_update(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    if request.method == "POST":
        form = ClientesForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClientesForm(instance=cliente)
    return render(request, 'clientes/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'clientes/cliente_confirm_delete.html', {'cliente': cliente})