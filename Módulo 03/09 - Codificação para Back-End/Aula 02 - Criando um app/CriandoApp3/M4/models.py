from django.db import models
class atirador(models.Model):
    nome = models.CharField(max_length=50)
class snaper(models.Model):
    nome = models.CharField(max_length=50)
class mediaDisparo(models.Model):
    media = models.PositiveBigIntegerField()

# Create your models here.
