from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='item-list'),
    path('item/<int:pk>/', views.detailList.as_view(), name='item-detail'),
    path('item/new/', views.ItemCreate.as_view(), name='item-create'),
]
