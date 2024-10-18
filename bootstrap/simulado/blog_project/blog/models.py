# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    deslikes = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor} no post {self.post}"

class Interaction(models.Model):
    TIPOS = (('like', 'Like'), ('dislike', 'Dislike'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_interacao = models.CharField(choices=TIPOS, max_length=7)

    class Meta:
        unique_together = ('post', 'user')  # Limitar para uma interação por usuário

