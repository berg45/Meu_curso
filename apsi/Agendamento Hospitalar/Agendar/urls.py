from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_visitas, name='listar_visitas'),
    path('agendar/', views.agendar_visita, name='agendar_visita'),
]
