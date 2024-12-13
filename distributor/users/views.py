from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group  # Para manejar roles

class RegisterCommonUserView(APIView):
    """
    Vista para registrar usuarios comunes (clientes).
    """
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Guardamos el usuario

            # Asignamos el rol de usuario común
            user.role = 'common_user'
            user.save()

            # Generamos tokens para el usuario registrado
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "message": "Usuario común registrado exitosamente.",
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh)
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterEmployeeAdminView(APIView):
    """
    Vista para registrar empleados y administradores.
    Nota: Se requiere un token JWT de un administrador para acceder.
    """
    def post(self, request):
        if not request.user.is_authenticated or request.user.role != 'admin':
            return Response(
                {"message": "No tiene permisos para registrar empleados o administradores."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Verificamos y asignamos el rol
            role = request.data.get('role', 'employee')
            if role not in ['admin', 'employee']:
                return Response(
                    {"message": "El rol debe ser 'admin' o 'employee'."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user.role = role
            user.save()

            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "message": f"Usuario {role} registrado exitosamente.",
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh)
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Vista para iniciar sesión.
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Validamos las credenciales del usuario
        user = authenticate(username=username, password=password)
        if user:
            # Generamos tokens si las credenciales son válidas
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "Inicio de sesión exitoso.",
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                    "role": user.role  # Incluimos el rol del usuario
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {"message": "Credenciales inválidas."},
            status=status.HTTP_401_UNAUTHORIZED
        )
