

from django.shortcuts import render, get_object_or_404, redirect
from core.models import Produto
from django.http import HttpResponse


def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'detalhes_produto.html', {'produto': produto})


def carrinho_view(request):
    carrinho = request.session.get('carrinho', {})
    produtos = Produto.objects.filter(id__in=carrinho.keys())
    return render(request, 'api/carrinho.html', {'produtos': produtos, 'carrinho': carrinho})


def adicionar_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    if str(produto_id) in carrinho:
        carrinho[str(produto_id)] += 1
    else:
        carrinho[str(produto_id)] = 1
    request.session['carrinho'] = carrinho
    return redirect('carrinho_view')


def remover_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    if str(produto_id) in carrinho:
        del carrinho[str(produto_id)]
    request.session['carrinho'] = carrinho
    return redirect('carrinho_view')
