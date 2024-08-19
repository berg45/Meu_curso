from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=50)
    nota_final = models.IntegerField()

    def __str__(self):
        return self.nome
    
