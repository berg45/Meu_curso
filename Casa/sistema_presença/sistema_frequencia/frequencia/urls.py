# frequencia/urls.py

from django.urls import path
from . import views



urlpatterns = [
    path('marcar_presenca/<int:aluno_id>/', views.marcar_presenca, name='marcar_presenca'),
    path('detalhe_aluno/<int:aluno_id>/', views.detalhe_aluno, name='detalhe_aluno'),
    path('turma/<int:turma_id>/alunos/', views.lista_alunos, name='lista_alunos'),
]
