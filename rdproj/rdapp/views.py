from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

# Create your views here.


class UserViewList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
