from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    TAMANHO = (
        ("P", "Pequeno"),
        ("M", "Médio"),
        ("G", "Grande")
    )
    nome_produto = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    tamanho = models.CharField(max_length=2, choices=TAMANHO)
    estoque = models.PositiveIntegerField(default=0)  # Quantidade no estoque

    def __str__(self):
        return self.nome_produto


class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='ItemCarrinho')

    def __str__(self):
        return f"Carrinho de {self.usuario.username}"


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome_produto} no carrinho"


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Pedido {self.id} de {self.usuario.username}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome_produto} no pedido"
