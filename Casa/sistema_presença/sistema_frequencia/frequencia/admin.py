from django.contrib import admin
from .models import Aluno, Turma, Presenca

admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(Presenca)
