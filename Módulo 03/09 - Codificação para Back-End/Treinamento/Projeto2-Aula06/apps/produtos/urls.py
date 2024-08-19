from django.urls import path
from .views import *

urlpatterns = [
        path('lista-produtos/', inicial, name="pagina_inicial"),
        #path("", inicial, name="pagina_inicial"),
	path("cadastro/", login, name="pagina_login"),
        
	]