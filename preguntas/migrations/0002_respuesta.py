# Generated by Django 2.2.11 on 2020-03-22 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preguntas.Pregunta')),
            ],
        ),
    ]
