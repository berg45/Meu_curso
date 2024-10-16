from django.db import models

class Produtos(models.Model):
    nome_produto = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="foto_produto/")
    descricao = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=10 , verbose_name="Preço")
