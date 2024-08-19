from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=40)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class Genero(models.Model):
    TIPO_SEXO = (
       ("M", "Masculino"),
       ("F", "Feminino")
    )
    sexo = models.CharField(max_length=2, choices=TIPO_SEXO)

    
    
