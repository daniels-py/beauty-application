from rest_framework import serializers
from .models import CustomUser

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'phone_number',
            'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'is_online'
        ]
        extra_kwargs = {
            'email': {'validators': []},  # Eliminar validadores predeterminados para agregar uno personalizado
        }

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está en uso.")
        return value