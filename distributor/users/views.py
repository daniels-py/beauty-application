from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate

class RegisterView(APIView):
    """
    Vista para registrar nuevos usuarios.
    """
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Guardamos el usuario

            # Generamos tokens de acceso y refresh para el usuario recién registrado
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "message": "Usuario registrado exitosamente.",
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
            # Generamos tokens de acceso y refresh si las credenciales son válidas
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "Inicio de sesión exitoso.",
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh)
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {"message": "Credenciales inválidas."},
            status=status.HTTP_401_UNAUTHORIZED
        )