from django.urls import path
from .views import *

urlpatterns = [
    path("", VerDeposito, name="pagina_deposito")
]