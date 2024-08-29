from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='lista_produtos'),
    path('produto/<int:pk>/', views.ProdutoDetailView.as_view(), name='detalhes_produto'),
    path('produto/new/', views.ProdutoCreateView.as_view(), name='criar_produto'),
    path('produto/<int:pk>/edit/', views.ProdutoUpdateView.as_view(), name='editar_produto'),
    path('produto/<int:pk>/delete/', views.ProdutoDeleteView.as_view(), name='deletar_produto'),
]
