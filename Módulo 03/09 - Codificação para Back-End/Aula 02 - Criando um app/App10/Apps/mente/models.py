from django.db import models

class cadPessoa(models.Model):
    nome = models.CharField(max_length=65)
    data_nascimento = models.DateField()
    cpf = models.PositiveBigIntegerField()
    email = models.EmailField()

class generos(models.Model):    
    Tipo_sexo = (
        ("Masculino"),
        ("Femenino")
    )
    sexo = models.CharField(max_length=2, choices=Tipo_sexo)
    
