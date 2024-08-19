from django.db import models

class usuario(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField()
    cpf = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
    
