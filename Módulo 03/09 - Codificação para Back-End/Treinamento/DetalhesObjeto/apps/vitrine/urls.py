from django.urls import path
from .views import *

urlpatterns = [
    path("", VerProdutos, name="minha_loja"),
    path("verproduto/<int:id_produto>/", DetalhesProduto, name="detalhes_produto")
]