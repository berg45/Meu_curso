from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('produtos/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
    path('produtos/novo/', views.criar_produto, name='criar_produto'),
    path('produtos/<int:produto_id>/editar/', views.editar_produto, name='editar_produto'),
    path('produtos/<int:produto_id>/deletar/', views.deletar_produto, name='deletar_produto'),
]
