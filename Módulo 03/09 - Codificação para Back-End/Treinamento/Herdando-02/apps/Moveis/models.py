from django.db import models

class Movel(models.Model):
    nome = models.CharField(max_length=60)
    categoria = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to="imagem/")
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome
    
class Cadastro(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cpf = models.PositiveBigIntegerField()
    
    crear_senha = models.CharField(max_length=15)
    confirmar_senha = models.CharField(max_length=50)    

    def __str__(self):
        return self.nome
    
