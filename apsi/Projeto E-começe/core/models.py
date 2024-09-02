from django.db import models

class Produto(models.Model):
    img_produto = models.ImageField(upload_to="imagem_produto/")
    nome_produto = models.CharField(max_length=40)
    descricao = models.TextField(max_length=200)
    valorComDesconto = models.DecimalField(decimal_places=2, max_digits=6)
    valorSemDesconto = models.DecimalField(decimal_places=2, max_digits=6)
    

    def __str__(self):
        return self.nome_produto
    

class Clientes(models.Model):
        id = models.AutoField(primary_key=True)
        nome = models.CharField(max_length=150)
        cpf_cnpj = models.CharField(max_length=150)
        cep = models.TextField(max_length=8)
        endereço = models.TextField(max_length=150)
        bairro = models.TextField(max_length=150)
        numero = models.TextField(max_length=5)
        cidade = models.TextField(max_length=30)
        estado = models.TextField(max_length=3)
      

        def __str__(self):
            return self.nome