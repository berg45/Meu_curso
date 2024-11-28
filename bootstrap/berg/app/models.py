from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='posts/', blank=True, null=True)  # Para armazenar imagens
    data_criacao = models.DateTimeField(auto_now_add=True)

    def contar_curtidas(self):
        return self.curtidas.count()
    

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.usuario.username} no post {self.post.titulo}'

class Curtida(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='curtidas', on_delete=models.CASCADE)  
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'post')  

  
