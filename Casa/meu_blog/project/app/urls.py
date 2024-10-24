# app/urls.py

from django.urls import path
from .views import lista_postagens, detalhes_postagem, adicionar_curtida
from . import views

urlpatterns = [
    path('', lista_postagens, name='lista_postagens'),
    path('post/<int:post_id>/', detalhes_postagem, name='detalhes_postagem'),
    path('novo/', views.post_create, name='post_create'),
    path('<int:pk>/editar/', views.post_update, name='post_update'),
    path('<int:pk>/deletar/', views.post_delete, name='post_delete'),
    path('post/<int:post_id>/comentario/', views.adicionar_comentario, name='adicionar_comentario'),
    path('adicionar_curtida/<int:post_id>/', adicionar_curtida, name='adicionar_curtida'),
   
]
