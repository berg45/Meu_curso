from django.db import models

    
class professor(models.Model):
    nome = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    salario = models.FloatField()

    def __str__(self):
        return self.nome
    
 