from django.urls import path
from .views import PostListCreate, PostDetail 
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)



urlpatterns = [
   path('posts/', PostListCreate.as_view(), name='post-list-create'),
   path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),

]
