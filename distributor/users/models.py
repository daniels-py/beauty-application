from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('employee', 'Empleado'),
        ('common_user', 'Usuario Común'),
    )
    email = models.EmailField(unique=True)  # Hacer el correo electrónico único
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_online = models.BooleanField(default=False)  # Campo para indicar si el usuario está conectado

    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='common_user')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
