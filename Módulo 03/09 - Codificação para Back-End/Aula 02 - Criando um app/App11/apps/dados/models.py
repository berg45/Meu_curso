from django.db import models

#class aluno(models.Model):

class escolaridade(models.Model):
    grau_escola = (
        ("P","Primario"),
        ("F","Fundamento"),
        ("M","Medio"),
        ("S","Superior")
    )


    nome = models.CharField(max_length=45)
    data_nascimento =models.DateField()
    cpf =  models.PositiveBigIntegerField()
    email = models.EmailField()
    Estudante = models.CharField(max_length=2, choices= grau_escola)
    valor = models.DecimalField(max_digits=4, decimal_places=2)



    

    def __str__(self):
        return self.nome
    



   
    
  