from django.db import models

class Produto(models.Model):
    img_produto = models.ImageField(upload_to="imagem_produto/")
    nome_produto = models.CharField(max_length=40)
    descricao = models.TextField(max_length=200)
    valorComDesconto = models.DecimalField(decimal_places=2, max_digits=10)
    valorSemDesconto = models.DecimalField(decimal_places=2, max_digits=10)
    
    

    def __str__(self):
        return self.nome_produto
    

class Clientes(models.Model):
        id = models.AutoField(primary_key=True)
        nome = models.CharField(max_length=150)
        cpf_cnpj = models.CharField(max_length=150)
        email = models.EmailField()
        cep = models.TextField(max_length=8)
        endereco = models.TextField(max_length=150)
        bairro = models.TextField(max_length=150)
        numero = models.TextField(max_length=5)
        cidade = models.TextField(max_length=30)
        estado = models.TextField(max_length=3)
      

        def __str__(self):
            return self.nome
        
class Compra(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True, blank=True)
    produtos = models.ManyToManyField(Produto, through='ItemCompra')
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_compra = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Compra {self.id} - Cliente: {self.cliente.nome if self.cliente else 'Sem cliente'}"

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra,  on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.produto.preco * self.quantidade