from django.urls import path
from .views import *

urlpatterns = [
    path("", VerPacientes, name="pg_inicial"),
]