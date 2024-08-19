from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=30)
    valor_produto = models.DecimalField(decimal_places=2, max_digits=5)
    imagem_produto = models.ImageField(upload_to="imagem_produto/" 
                                       )

    def __str__(self):
        return self.nome_produto
    
