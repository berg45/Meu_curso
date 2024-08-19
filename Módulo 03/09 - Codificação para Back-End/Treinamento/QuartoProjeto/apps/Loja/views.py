from django.shortcuts import render

from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Olá mundo!!!")
def jumento(request):
    return render(request, "ola_mundo.html")


