from django.contrib.auth.models import User
from django.db import models
class Usuario(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=128)  # A senha será armazenada em texto puro
    foto = models.ImageField(upload_to='static/fotos_usuarios/', null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UsuarioManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'nickname']

    def __str__(self):
        return self.email

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

