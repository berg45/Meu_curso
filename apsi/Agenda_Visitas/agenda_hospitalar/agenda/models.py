from django.db import models
from django.core.exceptions import ValidationError

class Visitante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Visita(models.Model):
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()

    def __str__(self):
        return f"{self.visitante.nome} - {self.data_hora}"

    def clean(self):
       
        visitas_no_horario = Visita.objects.filter(data_hora=self.data_hora).count()
        if visitas_no_horario >= 2:
            raise ValidationError('Este horário já foi escolhido duas vezes.')

    def save(self, *args, **kwargs):
       
        self.clean()
        super().save(*args, **kwargs)

