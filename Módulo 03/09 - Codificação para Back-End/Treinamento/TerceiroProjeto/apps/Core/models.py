from django.db import models

class Produtos(models.Model):
    nome = models.CharField("nome" max_length=50)
    preco =  models.DecimalField(
        "preço", decimal_places=2, max_digits=5)
    imagem = models.ImageField("imagem/")
    manual = models.FileField("pdfs/")

    def __str__(self):
        return self.nome
    
