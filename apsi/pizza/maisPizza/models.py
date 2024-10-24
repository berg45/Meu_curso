from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    cep = models.TextField(max_length=11)
    endereco = models.TextField(max_length=40)
    bairro = models.TextField(max_length=30)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    TAMANHO_P = (
        ("P", "Pequena"),
        ("M", "Média"),
        ("G", "Grande")
    )

    TIPO_PEDIDO = (
        ("NL", "No local"),
        ("D", "Delivery")
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relacionamento com Cliente
    sabor = models.CharField(max_length=40)
    tamanho = models.CharField(max_length=2, choices=TAMANHO_P)
    pedido = models.CharField(max_length=2, choices=TIPO_PEDIDO)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.sabor} - {self.get_tamanho_display()} ({self.cliente.nome})"

