from django.urls import path

from . import views 

urlpatterns = [
    path('publicacoes/', views.lista_publicacoes, name='lista_publicacoes'),
    path('publicacoes/nova/', views.criar_publicacao, name='criar_publicacao'),
    path('publicacoes/editar<int:pk>/', views.editar_publicacao, name='editar_publicacao'),
    path('publicacoes/excluir/<int:pk>/', views.excluir_publicacao, name='excluir_publicacao'),
]


