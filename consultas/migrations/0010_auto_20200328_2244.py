# Generated by Django 2.2.11 on 2020-03-29 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0009_auto_20200327_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nombre_y_apellidos',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=100),
        ),
    ]
