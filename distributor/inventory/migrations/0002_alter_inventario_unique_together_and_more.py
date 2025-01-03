# Generated by Django 5.1.4 on 2024-12-30 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('products', '0002_remove_cartacolor_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inventario',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='producto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventario', to='products.producto'),
        ),
    ]