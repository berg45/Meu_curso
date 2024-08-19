from django.shortcuts import render

def LinkInicial(request):
    return render(request, "index.html")
def Linklongin(request):
    return render(request, "longin.html")