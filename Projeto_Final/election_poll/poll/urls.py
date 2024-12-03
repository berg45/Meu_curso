from django.urls import path
from . import views

urlpatterns = [
    path('', views.poll_list, name='poll_list'),
    path('poll/<int:id>/', views.poll_detail, name='poll_detail'),
    path('poll/<int:id>/vote/', views.vote, name='vote'),
    path('poll/<int:id>/results/', views.poll_results, name='poll_results'),
    path('poll/create/', views.create_poll, name='create_poll'),
    path('poll/<int:id>/delete/', views.delete_poll, name='delete_poll'),
]
