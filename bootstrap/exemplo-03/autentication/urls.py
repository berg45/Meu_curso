from django.urls import path
from django.contrib.auth import views as auth_views
from autentication.views import register
from django.views.generic import TemplateView
from autentication.views import login_view

urlpatterns = [
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'),name='dashboard'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]