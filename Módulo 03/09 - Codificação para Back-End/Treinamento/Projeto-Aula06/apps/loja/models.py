from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=24)
    valor_produto = models.DecimalField(decimal_places=2, max_digits=5)
  
