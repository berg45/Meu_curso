from decimal import Decimal
from django.conf import settings
from core.models import Produto

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            # Usando valorComDesconto como o campo de preço
            self.cart[product_id] = {
                'quantity': 0, 
                'price': str(product.valorComDesconto)
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Marca a sessão como modificada para garantir que o carrinho seja salvo
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Produto.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # Retorna a quantidade total de itens no carrinho
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        # Calcula o preço total de todos os itens no carrinho
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # Limpa o carrinho removendo-o da sessão
        del self.session[settings.CART_SESSION_ID]
        self.save()
