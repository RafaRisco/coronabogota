# Generated by Django 2.2.11 on 2020-03-22 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0001_initial'),
        ('preguntas', '0002_respuesta'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='consulta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='consultas.Consulta'),
        ),
    ]