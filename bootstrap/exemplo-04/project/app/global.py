from .models import Empresa, Publicacao

def empresas(request):
    empresas = Empresa.objects.first()
    return{
        'empresas': empresas
    }

def publicacao(requst):
    publicacao = Publicacao.objects.all()
    return{
        'publicacao': publicacao
    }