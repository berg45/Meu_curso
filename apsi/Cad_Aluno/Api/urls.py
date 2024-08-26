from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('aluno/<int:aluno_id>/', views.detalhe_aluno, name='detalhe_aluno'),
    path('adicionar/', views.adicionar_aluno, name='adicionar_aluno'),
    path('editar/<int:aluno_id>/', views.editar_aluno, name='editar_aluno'),
    path('excluir/<int:aluno_id>/', views.excluir_aluno, name='excluir_aluno'),
]
