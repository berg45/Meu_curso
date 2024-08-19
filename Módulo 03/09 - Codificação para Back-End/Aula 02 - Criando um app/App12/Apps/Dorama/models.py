from django.db import models

class filmes(models.Model):
    classificacao = (
        ("AC","Ação"),
        ("FI","Ficção"),
        ("DR","Drama"),
        ("AV","Aventura"),
        ("TR","Terro")
    )
    filme = models.CharField(max_length=2, choices=classificacao)
    preco = models.DecimalField(max_digits=4, decimal_places=2)
    

    
    def __str__(self):
        return self.filme
    
    
