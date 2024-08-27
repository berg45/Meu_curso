from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="foto_perfil/")
    estado = models.CharField(max_length=15)
    cidade =  models.CharField(max_length=100) 

    def __str__(self):
        return self.nome  
