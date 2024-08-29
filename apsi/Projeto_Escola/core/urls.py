from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alunos, name='listar_alunos'),
    path('alunos/novo/', views.criar_aluno, name='criar_aluno'),
    path('alunos/<int:aluno_id>/editar/', views.atualizar_aluno, name='atualizar_aluno'),
    path('alunos/<int:aluno_id>/excluir/', views.excluir_aluno, name='excluir_aluno'),
    path('alunos/<int:aluno_id>/', views.detalhes_aluno, name='detalhes_aluno'),
    # Adicione outras rotas para Professores, Turmas, Disciplinas, Notas, etc.
]
