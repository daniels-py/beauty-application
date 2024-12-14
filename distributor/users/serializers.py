from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    role = serializers.CharField(write_only=True, required=False, allow_blank=True)  # Añadimos 'role' opcional

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'confirm_password', 'email', 'first_name', 'last_name', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        """
        Validamos:
        - Que las contraseñas coincidan.
        - Que la longitud de la contraseña sea adecuada.
        - Validamos el 'role' si es proporcionado.
        """
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})

        if len(password) < 6:
            raise serializers.ValidationError({"password": "La contraseña debe tener al menos 6 caracteres."})

        # Validación para el campo 'role'
        role = data.get('role', 'common_user')  # Si no se proporciona, se asigna 'common_user'
        if role not in ['admin', 'employee', 'common_user']:
            raise serializers.ValidationError({"role": "El rol debe ser 'admin', 'employee' o 'common_user'."})

        return data

    def create(self, validated_data):
        """
        Creamos el usuario:
        - Si el 'role' no está presente, se asigna automáticamente 'common_user'.
        """
        validated_data.pop('confirm_password')
        
        # Si no se ha enviado el campo 'role', se asigna 'common_user' por defecto
        role = validated_data.get('role', 'common_user')
        
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        
        # Asignamos el rol
        user.role = role
        user.save()

        return user
