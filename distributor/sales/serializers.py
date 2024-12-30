from rest_framework import serializers
from .models import Venta

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id', 'fecha', 'producto', 'cantidad', 'total']
