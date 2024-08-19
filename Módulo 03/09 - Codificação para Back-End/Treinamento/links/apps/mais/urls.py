from django.urls import path
from .views import *

urlpatterns = [
    	path("", LinkInicial, name="pagina_inicial"),
		path("cadastro", Linklongin, name="pagina_cadastro"),
	]