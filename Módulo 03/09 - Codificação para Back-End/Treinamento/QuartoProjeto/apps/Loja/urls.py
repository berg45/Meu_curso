from django.urls import path
from .views import *
urlpatterns = [
    	path('lista-produtos/', saudacao),
        path('jumento/', jumento)
	]