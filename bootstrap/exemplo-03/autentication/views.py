from django.shortcuts import render, redirect
from Core.models import Usuario  # Importe o seu modelo de usuário
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Usuario.objects.get(email=email)
            if user.senha == password:  # Verifica a senha diretamente
                login(request, user)  # Realiza o login do usuário
                
                # Verifica se existe um 'next' na requisição
                next_url = request.POST.get('next', None)
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return redirect('dashboard')  # Usa o LOGIN_REDIRECT_URL se não houver um 'next'
            else:
                messages.error(request, 'Senha incorreta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'E-mail não encontrado.')
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})


    