from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from core.models import *


def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'usuario/produtos.html', {'produtos': produtos})


def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'usuario/detalhes_produto.html', {'produto': produto})


def carrinho_view(request):
    carrinho = request.session.get('carrinho', {})
    produtos = Produto.objects.filter(id__in=carrinho.keys())
    return render(request, 'usuario/carrinho.html', {'produtos': produtos, 'carrinho': carrinho})


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



class FinalizacaoCompraView(TemplateView):
    template_name = 'usuario/finalizacao_compra.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        compra = get_object_or_404(Compra, pk=self.kwargs['pk'])
        cliente = compra.cliente  # Assumindo que a compra tem um campo relacionado ao cliente

        # Adiciona os objetos ao contexto
        context['compra'] = compra
        context['cliente'] = cliente
        return context


