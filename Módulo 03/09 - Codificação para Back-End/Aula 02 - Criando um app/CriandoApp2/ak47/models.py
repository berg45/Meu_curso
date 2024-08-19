from django.db import models

class dadosPessoa(models.Model):
    cpf = models.PositiveBigIntegerField()
