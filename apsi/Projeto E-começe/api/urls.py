from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto_list, name='lista_produtos'),
    path('produto/<int:pk>/', views.produto_detail, name='detalhes_produto'),
    path('carrinho/', views.carrinho_view, name='carrinho_view'),
    path('adicionar/<int:produto_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('remover/<int:produto_id>/', views.remover_carrinho, name='remover_carrinho'),
    path('user/finalizacao-compra/', views.FinalizacaoCompraView.as_view(), name='finalizacao_compra'),
    
]
