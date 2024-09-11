from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()
    professores = models.ManyToManyField(Professor)
    disciplinas = models.ManyToManyField('Disciplina')
    
    def __str__(self):
        return f'{self.nome} - {self.ano}'

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    data_avaliacao = models.DateField()

    def __str__(self):
        return f'{self.aluno} - {self.disciplina}: {self.nota}'
