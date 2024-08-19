from django.shortcuts import render

from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Fala Brow!!!")

def saudacao(request):
    return render(request, 'index.html')