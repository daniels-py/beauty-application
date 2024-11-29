from django.shortcuts import render
from rest_framework import viewsets
from .models import Inventario
from .serializers import InventarioSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
