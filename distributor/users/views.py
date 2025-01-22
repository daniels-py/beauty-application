from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
from .models import CustomUser
from .serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=['get'], url_path='total')
    def total_users(self, request):
        """
        Método para contar el número total de usuarios.
        """
        user_count = CustomUser.objects.count()
        return Response({'total_users': user_count}, status=status.HTTP_200_OK)