from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('usuario/novo/', views.criar_usuario, name='criar_usuario'),
    path('usuario/<int:aluno_id>/editar/', views.atualizar_usuario, name='atualizar_usuario'),
    path('usuario/<int:aluno_id>/excluir/', views.excluir_usuario, name='excluir_usuario'),
    path('usuario/<int:aluno_id>/', views.detalhes_usuario, name='detalhes_usuario'),
]