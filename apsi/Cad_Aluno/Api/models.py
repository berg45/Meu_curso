from django.db import models

class Aluno(models.Model):
    nome = models.CharField(100)
    estado = models.CharField(15)
    cidade =  models.CharField(100) 

    def __str__(self):
        return self.nome  
