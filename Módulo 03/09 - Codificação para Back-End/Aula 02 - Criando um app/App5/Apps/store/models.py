from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=40)
    cpf = models.PositiveBigIntegerField()
    email = models.EmailField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
