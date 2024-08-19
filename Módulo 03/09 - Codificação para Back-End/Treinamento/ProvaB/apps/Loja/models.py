from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField()
    senha = models.CharField(max_length=10)
    foto = models.ImageField(upload_to="foto_usuario")

    
    TIPO_SEXO = (
        ("M", "Masculino"),
        ("F", "Feminino")
    )
    sexo = models.CharField(max_length=2, choices=TIPO_SEXO)

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome_produto = models.CharField(max_length=25)
    valor_produto = models.DecimalField(max_digits=4, decimal_places=2)
    imagem = models.ImageField(upload_to="imagem_produto")

    def __str__(self):
        return self.nome_produto
    
class Login(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=10)
    
    def __str__(self):
        return self.email
    

