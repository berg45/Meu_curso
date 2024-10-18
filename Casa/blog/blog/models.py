from django.contrib.auth.models import User
from django.db import models

class Postagem(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    deslikes = models.ManyToManyField(User, related_name='deslikes', blank=True)

    def total_likes(self):
        return self.likes.count()

    def total_deslikes(self):
        return self.deslikes.count()

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} comentou: {self.texto[:20]}...'

