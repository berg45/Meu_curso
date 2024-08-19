from django.db import models

class Deposito(models.Model):
    nome_produto = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    

    def __str__(self):
        return self.nome_produto
    
