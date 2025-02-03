from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
from .models import Inventario
from .serializers import InventarioSerializer
from rest_framework import serializers


class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

    @action(detail=False, methods=['get'], url_path='stock')
    def total_inventario(self, request):
        inventario_count = Inventario.objects.count()
        return Response({'total_inventario': inventario_count}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        producto = serializer.validated_data['producto']
        # Validación adicional en la vista, por si no se validó en el serializer
        if Inventario.objects.filter(producto=producto).exists():
            raise serializers.ValidationError(f"El producto {producto.nombre} ya está en el inventario.")
        serializer.save()