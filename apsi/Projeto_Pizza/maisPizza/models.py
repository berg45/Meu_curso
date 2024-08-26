from django.db import models

class Pedidos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=3)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.nome
    
    
class Clientes(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=150)
        cpf_cnpj = models.CharField(max_length=150)
        zip_code = models.TextField(max_length=11)
        address = models.TextField(max_length=150)
        neighborhood = models.TextField(max_length=150)
        number = models.TextField(max_length=5)
        city = models.TextField(max_length=30)
        state = models.TextField(max_length=3)
        
        def __str__(self):
            return self.name
