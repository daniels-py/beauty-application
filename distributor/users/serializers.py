from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'phone_number',
            'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'is_online'
        ]

    def validate_email(self, value):
        """Evita que se registre un email duplicado, pero permite actualizarlo si es el mismo."""
        if self.instance:  # Si se está actualizando
            if self.instance.email != value and CustomUser.objects.filter(email=value).exists():
                raise serializers.ValidationError("Este correo electrónico ya está en uso.")
        else:  # Si se está creando
            if CustomUser.objects.filter(email=value).exists():
                raise serializers.ValidationError("Este correo electrónico ya está en uso.")
        return value


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    # Agregar campo de confirmación de contraseña
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "password2", "first_name", "last_name", "phone_number"]
        extra_kwargs = {
            "password": {"write_only": True},  # Asegurar que la contraseña solo sea escrita
        }

    def validate(self, data):
        """
        Validar que las contraseñas coincidan.
        """
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Las contraseñas no coinciden.")
        return data

    def create(self, validated_data):
        # Eliminar el campo 'password2' ya que no lo necesitamos al crear el usuario
        validated_data.pop('password2', None)
        
        # Crear el usuario con la contraseña encriptada
        validated_data["password"] = make_password(validated_data["password"])  # Encriptar la contraseña
        user = CustomUser.objects.create_user(**validated_data)
        user.role = "common_user"  # Asegurar que el rol sea siempre "Usuario Común"
        user.save()
        return user