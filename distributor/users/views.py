from .models import *
from .models import CustomUser
from rest_framework import viewsets
from .serializers import *
from django.shortcuts import render

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerializer


