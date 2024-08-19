from django.db import models

class Dados(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.PositiveBigIntegerField(null=True, blank=True)
    telefone = models.PositiveBigIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    etinia = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="foto_perfil/" ,null=True, blank=True)
    doc = models.FileField(upload_to= "documento/")


    def __str__(self):
        return self.nome
    
