from django.db import models

from consultas.models import Consulta
# Create your models here.

class Pregunta(models.Model):
    titulo      = models.CharField(max_length=500)

    def __str__(self):
        return str(self.pk)

class Respuesta(models.Model):
    consulta    = models.ForeignKey(Consulta, on_delete=models.DO_NOTHING, blank=True, null=True)
    pregunta    = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    titulo      = models.CharField(max_length=500)

    @property
    def titulo_pregunta(self):
        return self.pregunta.titulo

    @property
    def numero_consulta(self):
        return self.consulta.telefono

    def __str__(self):
        return str(self.pk)
