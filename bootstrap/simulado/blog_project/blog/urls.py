from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike/<int:post_id>/', views.dislike_post, name='dislike_post'),
]
