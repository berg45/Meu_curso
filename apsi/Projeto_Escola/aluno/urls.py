from django.urls import path
from . import views

urlpatterns = [
    path('', views.area_aluno, name='area_aluno'),
]