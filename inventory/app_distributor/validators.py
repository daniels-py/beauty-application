from django.core.exceptions import ValidationError
import re

class FlexiblePasswordValidator:
    def __init__(self, min_length=6):
        self.min_length = min_length

    def validate(self, password, user=None):
        # Verifica que la contraseña tenga al menos la longitud mínima
        if len(password) < self.min_length:
            raise ValidationError(f'La contraseña debe tener al menos {self.min_length} caracteres.')

        # Verifica que la contraseña contenga al menos un número
        if not re.search(r'\d', password):
            raise ValidationError('La contraseña debe contener al menos un número.')

        # Puedes añadir más reglas aquí si lo deseas
        # Por ejemplo, más adelante podrías requerir una letra mayúscula o caracteres especiales

    def get_help_text(self):
        return f'Tu contraseña debe tener al menos {self.min_length} caracteres y al menos un número.'
