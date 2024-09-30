from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.produto_list, name='lista_produtos'),
    path('produto/<int:pk>/', views.produto_detail, name='detalhes_produto'),
    path('carrinho/', views.carrinho_view, name='carrinho_view'),
    path('adicionar/<int:produto_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('remover/<int:produto_id>/', views.remover_carrinho, name='remover_carrinho'),
    #path('user/finalizacao-compra/<int:pk>/', views.FinalizacaoCompraView.as_view(), name='finalizacao_compra'),
    path('finalizar-compra/<int:cliente_id>/', views.finalizar_compra, name='finalizacao_compra'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
]
