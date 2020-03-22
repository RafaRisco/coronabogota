from django.db import models
from django.db.models.signals import post_save, pre_save

from consultas.models import Consulta
# Create your models here.

class Pregunta(models.Model):
    titulo      = models.CharField(max_length=500)

    def __str__(self):
        return str(self.pk)

class Respuesta(models.Model):
    consulta        = models.ForeignKey(Consulta, on_delete=models.DO_NOTHING, blank=True, null=True)
    pregunta        = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    titulo          = models.CharField(max_length=500)
    titulo_binario  = models.IntegerField(blank=True, null=True)

    @property
    def titulo_pregunta(self):
        return self.pregunta.titulo

    @property
    def numero_consulta(self):
        return self.consulta.telefono

    def __str__(self):
        return str(self.pk)

def respuesta_pre_save(instance, sender, *args, **kwargs):
    if instance.titulo_binario is None:
        if instance.titulo == 'Si':
            instance.titulo_binario = 1
        elif instance.titulo == 'No':
            instance.titulo_binario = 0

pre_save.connect(respuesta_pre_save, sender=Respuesta)        

def respuesta_post_save(instance, sender, created, *args, **kwargs):
    consulta = instance.consulta
    consulta.save()

post_save.connect(respuesta_post_save, sender=Respuesta)
