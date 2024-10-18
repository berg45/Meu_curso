from django.db import models

class Pizza(models.Model):

    TAMANHO = (
        ("P", "Pequena"),
        ("M", "Media"),
        ("G", "Grande"),
        ("GG", "Extra Grande")
    )
    tamanho = models.CharField(max_length=2, choices=TAMANHO)
    sabor = models.CharField(max_length=100)
    valor = models.DecimalField(decimal_places=2, max_digits=4)
    imagem = models.ImageField(upload_to="imagem_pizza/")

    def __str__(self):
        return f"{self.get_tamanho_display()} {self.sabor}"
    
class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantidade = models.PositiveBigIntegerField(default=1)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id}: {self.pizza} x {self.quantidade}"
