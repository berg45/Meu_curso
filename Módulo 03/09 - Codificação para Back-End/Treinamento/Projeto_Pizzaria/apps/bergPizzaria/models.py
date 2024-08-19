from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    descricao = models.CharField(max_length=200)
    data = models.DateField()

    def __str__(self):
        return self.descricao
    
