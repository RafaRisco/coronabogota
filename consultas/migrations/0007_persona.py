# Generated by Django 2.2.11 on 2020-03-28 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0006_validacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_y_apellidos', models.CharField(max_length=150)),
                ('dia_nacimiento', models.IntegerField()),
                ('mes_nacimiento', models.IntegerField()),
                ('año_nacimiento', models.IntegerField()),
                ('cedula', models.IntegerField()),
                ('sexo', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=150)),
            ],
        ),
    ]
