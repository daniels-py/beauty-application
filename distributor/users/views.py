from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import CustomUser
from .serializers import UsuarioSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .serializers import RegistroUsuarioSerializer
from django.views.generic import View
from django.shortcuts import render


class RegisterUserView(View):
    def get(self, request):
        return render( request, 'users/auth/register.html')



# Paginación personalizada
class UsuarioPagination(PageNumberPagination):
    page_size = 10  # Limitar los resultados por página

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerializer
    pagination_class = UsuarioPagination

    @action(detail=False, methods=['get'], url_path='total')
    def total_users(self, request):
        """
        Método para contar el número total de usuarios y los usuarios activos.
        """
        total_users = CustomUser.objects.count()
        active_users = CustomUser.objects.filter(is_active=True).count()
        return Response({
            'total_users': total_users,
            'active_users': active_users
        }, status=status.HTTP_200_OK)

class RegistroUsuarioView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistroUsuarioSerializer