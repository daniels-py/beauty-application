from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    # Campo adicional para confirmar la contraseña.
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'confirm_password', 'email', 'first_name', 'last_name', 'role']
        extra_kwargs = {
            'password': {'write_only': True},  # Hacemos que la contraseña sea de solo escritura (no se devuelve en las respuestas).
        }

    def validate(self, data):
        """
        Este método se usa para validar datos personalizados.
        Aquí verificamos:
        1. Que las contraseñas coincidan.
        2. Que la longitud de la contraseña sea mayor a 6 caracteres.
        """
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        # Validamos que ambas contraseñas coincidan
        if password != confirm_password:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})

        # Validamos que la contraseña tenga al menos 6 caracteres
        if len(password) < 6:
            raise serializers.ValidationError({"password": "La contraseña debe tener al menos 6 caracteres."})

        return data  # Si todo está bien, devolvemos los datos validados.

    def create(self, validated_data):
        """
        Método para crear el usuario.
        Aquí hacemos lo siguiente:
        1. Eliminamos el campo `confirm_password` del diccionario validado porque no se necesita para la creación.
        2. Creamos el usuario utilizando el modelo `CustomUser`.
        3. Encriptamos la contraseña usando `set_password`.
        """
        # Eliminamos `confirm_password` de los datos validados, ya no es necesario
        validated_data.pop('confirm_password')

        # Obtenemos la contraseña y creamos el usuario
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)

        # Encriptamos la contraseña antes de guardarla
        user.set_password(password)

        # Guardamos el usuario en la base de datos
        user.save()

        return user  # Retornamos el usuario creado
