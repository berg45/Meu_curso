from django.db import models

class dadospessoais(models.Model):
    nome = models.CharField(max_length=45)
    email = models.EmailField()
    senha = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    
    

class escolaridade(models.Model):
    Nivel_Ensino = (
        ("p","Primario"),
        ("F","Fundamental"),
        ("M","Médio"),
        ("S","Superior")
    )
    ensino = models.CharField(max_length=4, choices=Nivel_Ensino)
    valor = models.DecimalField(max_digits=4, decimal_places=2)



