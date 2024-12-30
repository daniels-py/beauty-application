from django.shortcuts import render
from rest_framework import viewsets
from .models import Inventario
from .serializers import InventarioSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet que habilita todas las operaciones CRUD para el modelo Inventario.
    """
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer