from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alunos, name='listar_alunos'),
    path('alunos/novo/', views.criar_aluno, name='criar_aluno'),
    path('alunos/<int:aluno_id>/editar/', views.atualizar_aluno, name='atualizar_aluno'),
    path('alunos/<int:aluno_id>/excluir/', views.excluir_aluno, name='excluir_aluno'),
    path('alunos/<int:aluno_id>/', views.detalhes_aluno, name='detalhes_aluno'),
    # Adicione outras rotas para Professores, Turmas, Disciplinas, Notas, etc.
    path('professores/', views.listar_professores, name='listar_professores'),
    path('professores/novo/', views.criar_professor, name='criar_professor'),
    path('professores/<int:professor_id>/editar/', views.atualizar_professor, name='atualizar_professor'),
    path('professores/<int:professor_id>/excluir/', views.excluir_professor, name='excluir_professor'),
    path('professores/<int:professor_id>/', views.detalhes_professor, name='detalhes_professor'),
     # Turma routes
    path('turmas/', views.listar_turmas, name='listar_turmas'),
    path('turmas/novo/', views.criar_turma, name='criar_turma'),
    path('turmas/<int:turma_id>/editar/', views.atualizar_turma, name='atualizar_turma'),
    path('turmas/<int:turma_id>/excluir/', views.excluir_turma, name='excluir_turma'),
    path('turmas/<int:turma_id>/', views.detalhes_turma, name='detalhes_turma'),

    # Disciplina routes
    path('disciplinas/', views.listar_disciplinas, name='listar_disciplinas'),
    path('disciplinas/novo/', views.criar_disciplina, name='criar_disciplina'),
    path('disciplinas/<int:disciplina_id>/editar/', views.atualizar_disciplina, name='atualizar_disciplina'),
    path('disciplinas/<int:disciplina_id>/excluir/', views.excluir_disciplina, name='excluir_disciplina'),
    path('disciplinas/<int:disciplina_id>/', views.detalhes_disciplina, name='detalhes_disciplina'),

    # Nota routes
    path('notas/', views.listar_notas, name='listar_notas'),
    path('notas/novo/', views.criar_nota, name='criar_nota'),
    path('notas/<int:nota_id>/editar/', views.atualizar_nota, name='atualizar_nota'),
    path('notas/<int:nota_id>/excluir/', views.excluir_nota, name='excluir_nota'),
    #path('notas/<int:nota_id>/', views.detalhes_nota, name='detalhes_nota'),
]
