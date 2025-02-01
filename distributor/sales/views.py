from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Venta, DetalleVenta
from .serializers import VentaSerializer, DetalleVentaSerializer




class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

    def create(self, request, *args, **kwargs):
        """
        Sobrescribimos el método `create` para manejar validaciones adicionales 
        o lógica personalizada durante la creación de una venta.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                # Intenta guardar la venta, actualizando el inventario en el proceso.
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer