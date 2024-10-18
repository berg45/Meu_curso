# app/urls.py

from django.urls import path
from .views import lista_postagens, detalhes_postagem

urlpatterns = [
    path('', lista_postagens, name='lista_postagens'),
    path('post/<int:post_id>/', detalhes_postagem, name='detalhes_postagem'),
]
