from django.db import models

class produto(models.Model):
    nome_produto = models.CharField(max_length=30)
    valor = models.DecimalField(decimal_places=2, max_digits=5)
    imagem = models.ImageField(upload_to="imagem/")

    def __str__(self):
        return self.nome_produto
    

