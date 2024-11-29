from rest_framework import serializers
from .models import *


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id', 'producto', 'unidades']