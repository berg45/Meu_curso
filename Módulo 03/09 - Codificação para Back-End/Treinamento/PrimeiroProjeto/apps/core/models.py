from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    date_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
    
    
