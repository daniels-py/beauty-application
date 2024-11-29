from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('employee', 'Empleado'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

    def __str__(self):
        return self.username