# frequencia/models.py

from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.nome} ({self.ano})"

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="alunos")

    def __str__(self):
        return self.nome

class Presenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField(default=False)

    def __str__(self):
        status = "Presente" if self.presente else "Ausente"
        return f"{self.aluno.nome} - {status} em {self.data}"
