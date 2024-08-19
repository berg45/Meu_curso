from django.urls import path
from .views import *

urlpatterns = [
    	path('home/', VerProdutos, name="pagina_home"),
        path("inicial", LinkInicial, name="pagina_inicial"),
        path("cadastro", LinkCadastro, name="pagina_cadastro"),
		path("login", LinkLogin, name="pagina_login"),
	]