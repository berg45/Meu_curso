from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



def LayoutView(request):
    return render(request, 'index.html')

def register(request):
   if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
       form.save()
    return redirect('login') 
   else:
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
   
@login_required
def dashboard(request):
   return render(request, 'dashboard.html')


