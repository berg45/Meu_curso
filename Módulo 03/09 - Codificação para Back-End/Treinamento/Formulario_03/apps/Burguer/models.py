from django.db import models

class Hamburguer(models.Model):
    nome = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    
    TIPO_PEDIDO = (
        ("NL", "No local"),
        ("D", "Delivere")
    )
    pedido = models.CharField(max_length=2, choices=TIPO_PEDIDO)
