from django.shortcuts import render, get_object_or_404, redirect
from .models import Produtos
from .forms import ProdutoForm

# Listar produtos
def listar_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})

# Detalhes de um produto
def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produtos, id=produto_id)
    return render(request, 'produtos/detalhe_produto.html', {'produto': produto})

# Criar produto
def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/criar_produto.html', {'form': form})

# Editar produto
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produtos, id=produto_id)
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar_produto.html', {'form': form})

# Deletar produto
def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produtos, id=produto_id)
    if request.method == "POST":
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'produtos/deletar_produto.html', {'produto': produto})
