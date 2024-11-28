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
    produtos = []

    for produto_id, quantidade in carrinho.items():
        produto = Produto.objects.get(id=produto_id)
        produto.quantidade = quantidade
        produtos.append(produto)
    return render(request, 'usuario/carrinho.html', {'produtos': produtos})


def adicionar_carrinho(request, produto_id):
    
    produto = get_object_or_404(Produto, id=produto_id)
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

def finalizar_compra(request, cliente_id):
    cliente = get_object_or_404(Clientes, id=cliente_id)

    if request.method == 'POST':
        # Aqui você deve pegar os produtos que estão no carrinho
        # Supondo que você tenha uma forma de armazenar o carrinho na sessão ou em um modelo
        cart_items = request.session.get('cart', {})  # Supondo que o carrinho esteja armazenado na sessão
        
        compra = Compra(cliente=cliente)
        compra.save()
        
        total_compra = 0
        for produto_id, item in cart_items.items():
            produto = get_object_or_404(Produto, id=produto_id)
            quantidade = item['quantity']
            subtotal = produto.valorComDesconto * quantidade  # Alterado para usar valorComDesconto
            total_compra += subtotal
            
            ItemCompra.objects.create(compra=compra, produto=produto, quantidade=quantidade)

        return redirect('compra_finalizada', compra_id=compra.id)  # Remova o total aqui
     
    return render(request, 'usuario/compra_finalizada.html', {'cliente': cliente})



def compra_finalizada(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    itens_compra = ItemCompra.objects.filter(compra=compra)
    total = sum(item.produto.preco * item.quantidade for item in itens_compra)

    return render(request, 'usuario/compra_finalizada.html', {
        'cliente': compra.cliente,
        'cart': itens_compra,
        'total': total
    })




