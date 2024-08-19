from django.shortcuts import render
from rest_framework import generics
from apps.Core.models import Clientes
from .serializers import ClientesSerializer
from rest_framework import filters
from .permissions import IsOwnerOrReadOnly


class PostListCreate(generics.ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class PostListCreate(generics.ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Clientes.objects.all()
 serializer_class = ClientesSerializer
 permission_classes = [IsOwnerOrReadOnly]


