from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item-list'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('item/new/', views.ItemCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item-edit'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item-delet'),
    path('formulario/', views.FormularioView, name='formulario'),
    path('formulario/list', views.FormListView, name='form_list'),
    path('formulario/<int:pk>/delete', views.FormDeleteView, name='form_delete'),
    path('formulario/<int:pk>/detail', views.FormDetailView, name= 'form_detail'),
    path('formulario/<int:pk>/edit', views.FormUpdateView, name= 'form_edit')
]

