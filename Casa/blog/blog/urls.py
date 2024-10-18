from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('deslike/<int:post_id>/', views.deslike_post, name='deslike_post'),
    path('comentar/<int:post_id>/', views.comentar_post, name='comentar_post'),
]
