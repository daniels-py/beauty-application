# Generated by Django 5.1.4 on 2024-12-30 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartacolor',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='presentacion',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='descripcion',
        ),
    ]
