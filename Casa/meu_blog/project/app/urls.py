# app/urls.py

from django.urls import path
from .views import lista_postagens, detalhes_postagem
from . import views

urlpatterns = [
    path('', lista_postagens, name='lista_postagens'),
    path('post/<int:post_id>/', detalhes_postagem, name='detalhes_postagem'),
    path('novo/', views.post_create, name='post_create'),
    path('<int:pk>/editar/', views.post_update, name='post_update'),
    path('<int:pk>/deletar/', views.post_delete, name='post_delete'),
   
]
