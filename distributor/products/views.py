from rest_framework import viewsets
from .models import Categoria, Marca, Presentacion, CartaColor, Producto
from .serializers import CategoriaSerializer, MarcaSerializer, PresentacionSerializer, CartaColorSerializer, ProductoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict




class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    @action(detail=False, methods=['get'], url_path='total')
    def get_total_marcas(self, request):
        total_marcas = Marca.objects.count()
        return Response({'total_marcas': total_marcas})


class PresentacionViewSet(viewsets.ModelViewSet):
    queryset = Presentacion.objects.all()
    serializer_class = PresentacionSerializer


class CartaColorViewSet(viewsets.ModelViewSet):
    queryset = CartaColor.objects.all()
    serializer_class = CartaColorSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_data = self.get_serializer(queryset, many=True).data

        # Agrupar por marca
        grouped_data = defaultdict(list)
        for item in serialized_data:
            grouped_data[item['marca']].append(item)

        return Response(grouped_data)
    
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    @action(detail=False, methods=['get'], url_path='total')
    def total_productos(self, request):
        """
        Método para contar el número total de productos.
        """
        total_productos = Producto.objects.count()
        return Response({
            'total_productos': total_productos
        }, status=status.HTTP_200_OK)


