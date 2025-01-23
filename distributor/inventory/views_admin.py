from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
from .models import Inventario
from .serializers_admin import InventarioSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet que habilita todas las operaciones CRUD para el modelo Inventario.
    """
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

    @action(detail=False, methods=['get'], url_path='stock')
    def total_inventario(self, request):
        """
        Método para contar el número total de elementos en el inventario.
        """
        inventario_count = Inventario.objects.count()
        return Response({'total_inventario': inventario_count}, status=status.HTTP_200_OK)