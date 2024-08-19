from django.urls import path
from .views import *

urlpatterns = [
    path('',VerInicial),
    path('cadastro', VerCadastro)
]
