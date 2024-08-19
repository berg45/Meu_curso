from django.db import models

class aluno(models.Model):
    nome = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    matricula = models.PositiveBigIntegerField()

    def __str__(self):
        return self.nome
    
