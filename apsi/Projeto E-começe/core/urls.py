from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
   
    path('', views.ProdutoListView.as_view(), name='lista_produtos'),
    path('produto/<int:pk>/', views.ProdutoDetailView.as_view(), name='detalhes_produto'),
    path('produto/new/', views.ProdutoCreateView.as_view(), name='criar_produto'),
    path('produto/<int:pk>/edit/', views.ProdutoUpdateView.as_view(), name='editar_produto'),
    path('produto/<int:pk>/delete/', views.ProdutoDeleteView.as_view(), name='deletar_produto'),

    # Formulario Clientes....
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('cliente/new/', views.cliente_create, name='cliente_create'),
    path('cliente/<int:pk>/edit/', views.cliente_update, name='cliente_update'),
    path('cliente/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
    

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
