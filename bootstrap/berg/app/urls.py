
from django.urls import path
from .views import lista_postagens, detalhes_postagem
from . import views

urlpatterns = [
    path('', lista_postagens, name='home_postagens'),
    path('post/<int:post_id>/', detalhes_postagem, name='detalhes_postagem'),

]