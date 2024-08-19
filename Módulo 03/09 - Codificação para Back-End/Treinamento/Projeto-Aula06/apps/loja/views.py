from django.shortcuts import render

def saudacao(request):
    return render(request, 'ola_mundo.html')
