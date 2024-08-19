from django.urls import path
from .views import *

urlpatterns = [
    path('', VerIndex),
    path('Login', VerLogin),
    path('Produtos', VerProdutos)
]
