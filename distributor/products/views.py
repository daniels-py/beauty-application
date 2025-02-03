from rest_framework import viewsets
from .models import Categoria, Marca, Presentacion, CartaColor, Producto
from .serializers import CategoriaSerializer, MarcaSerializer, PresentacionSerializer, CartaColorSerializer, ProductoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend



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



class ProductoPagination(PageNumberPagination):
    page_size = 10  # Número de productos por página
    page_size_query_param = 'page_size'
    max_page_size = 50


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.select_related('marca', 'categoria', 'presentacion').order_by('nombre')  # Agregado el ordenamiento por nombre
    serializer_class = ProductoSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]  # Solo usuarios autenticados pueden modificar
    pagination_class = ProductoPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['marca', 'categoria', 'presentacion']

    @action(detail=False, methods=['get'], url_path='total')
    def total_productos(self, request):
        """
        Devuelve el número total de productos.
        """
        total_productos = Producto.objects.count()
        return Response({'total_productos': total_productos}, status=status.HTTP_200_OK)
