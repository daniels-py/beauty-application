from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('employee', 'Empleado'),
        ('common_user', 'Usuario Común'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='common_user')

    def __str__(self):
        # Aquí puedes modificar la representación para usar el nombre completo
        return f"{self.first_name} {self.last_name}"
