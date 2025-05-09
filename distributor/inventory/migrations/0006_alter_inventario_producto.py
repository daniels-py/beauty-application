# Generated by Django 5.1.5 on 2025-02-01 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_inventario_fecha_ingreso_and_more'),
        ('products', '0005_alter_producto_carta_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario_inventory', to='products.producto'),
        ),
    ]
