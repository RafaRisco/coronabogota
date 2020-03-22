from django.db import models

# Create your models here.

class Pregunta(models.Model):
    titulo      = models.CharField(max_length=500)

    def __str__(self):
        return str(self.pk)

class Respuesta(models.Model):
    pregunta    = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    titulo      = models.CharField(max_length=500)

    def __str__(self):
        return str(self.pk)
