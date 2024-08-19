from django.db import models

class dadosPessoais(models.Model):
    nome = models.CharField(max_length=45)
    rg = models.PositiveBigIntegerField()
    cpf = models.PositiveBigIntegerField()
    data_nascimento = models.DateField()
    profisao = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    
class genero(models.Model):
    tipo_sexo = (
        ("M", "Masculino"),
        ("F", "Feminino")
    )
    sexo = models.CharField(max_length=2, choices=tipo_sexo)
    valor = models.DecimalField(max_digits=4, decimal_places=2)

    #class precoProduto(models.Model):    
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")

    
