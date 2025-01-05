from rest_framework import serializers
from .models import Venta


class VentaSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Venta
        fields = ['id', 'fecha', 'producto', 'cantidad', 'total']
