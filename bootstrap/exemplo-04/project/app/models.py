from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O endereço de email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.senha = password  # Armazena a senha diretamente
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

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

  
    def check_password(self, raw_password):
        return self.senha == raw_password

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Publicacao(models.Model):
    id_publicacao = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='publicacoes/', null=True, blank=True)
    titulo_prato = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='publicacoes')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo_prato

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE, related_name='comentarios')
    conteudo = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comentário de {self.usuario} na publicação {self.publicacao}'

class Curtida(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='curtidas')
    publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE, related_name='curtidas')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario} curtiu {self.publicacao}'
