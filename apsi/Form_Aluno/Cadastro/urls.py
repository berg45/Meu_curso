from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item-list'),
    path('item/new/', views.CreateView.as_view(), name='item-create'),
]