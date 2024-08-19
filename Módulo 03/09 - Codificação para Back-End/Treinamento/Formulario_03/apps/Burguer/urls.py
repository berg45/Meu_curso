from django.urls import path
from .views import *

urlpatterns = [
    path("", CriarHamburguer, name="pagina_inicial")
]