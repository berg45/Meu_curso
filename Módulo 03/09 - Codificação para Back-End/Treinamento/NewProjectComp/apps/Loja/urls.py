from django.urls import path
from .views import *

urlpatterns = [
    path('lista-produtos/', VerProdutos, name='pagina_index'),
   
    path("cadastro", LinkCadastro, name='pagina_login'),
]