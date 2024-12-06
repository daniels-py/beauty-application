from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('employee', 'Empleado'),
        ('common_user', 'Usuario Común'),  # Rol adicional para usuarios comunes
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='common_user')

    def __str__(self):
        return self.username



