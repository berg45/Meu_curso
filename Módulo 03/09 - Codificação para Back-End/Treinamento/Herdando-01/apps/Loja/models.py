from django.db import models

class Livros(models.Model):
    titulo_livro = models.CharField(max_length=30)
    nome_autor = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to="imagem/")
    valor = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.titulo_livro
    


