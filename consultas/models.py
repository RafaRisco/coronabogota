from django.db import models
from django.db.models.signals import post_save
from django.db.models import Avg

# Create your models here.

class Consulta(models.Model):
    telefono    = models.CharField(max_length=10)
    lat         = models.DecimalField(max_digits=9,decimal_places=6)
    long        = models.DecimalField(max_digits=9,decimal_places=6)
    address     = models.CharField(max_length=100, blank=True, null=True)
    dia         = models.DateTimeField(auto_now_add=True)
    gravedad    = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

def consulta_post_save(instance, sender, created, *args, **kwargs):
    respuestas = instance.respuesta_set.all()
    promedio = instance.respuesta_set.all().aggregate(Avg('titulo_binario'))
    valor_promedio = promedio['titulo_binario__avg']
    for respuesta in respuestas:
        print(respuesta.titulo)

post_save.connect(consulta_post_save, sender=Consulta)
