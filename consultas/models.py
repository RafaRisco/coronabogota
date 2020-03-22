from django.db import models

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
