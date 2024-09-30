from django.urls import path
from .views import register
from . import views




urlpatterns = [
    path('', views.LayoutView, name='index'),
    path('register/', views.register, name='register'),
    path('dashboard/',  views.dashboard, name='dashboard'),
    
]
