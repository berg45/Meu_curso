from django.shortcuts import render, redirect
from django.views.generic import *
from .models import Aluno 



class ItemListView(ListView):
    model = Aluno
    template_name = 'Cadastro/aluno_list.html'

class Createview():
    model = Aluno
    fields = ['nome', 'estado', 'preco']
    success_url = '/'
    template_name = 'Cadastro/create_aluno.html'
