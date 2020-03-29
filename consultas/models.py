from django.db import models
from django.db.models.signals import post_save
from django.db.models import Avg

# Create your models here.

SEXO_OPCIONES = (
    ('Hombre', 'Hombre'),
    ('Mujer', 'Mujer')
)

class Persona(models.Model):
    nombre_y_apellidos = models.CharField(max_length=150)
    dia_nacimiento     = models.PositiveIntegerField()
    mes_nacimiento     = models.PositiveIntegerField()
    año_nacimiento     = models.PositiveIntegerField()
    cedula             = models.PositiveIntegerField()
    sexo               = models.CharField(max_length=100, choices=SEXO_OPCIONES, blank=True, null=True)
    direccion          = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre_y_apellidos

class Consulta(models.Model):
    ciudadano   = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)
    telefono    = models.CharField(max_length=10)
    lat         = models.DecimalField(max_digits=9,decimal_places=6)
    long        = models.DecimalField(max_digits=9,decimal_places=6)
    address     = models.CharField(max_length=100, blank=True, null=True)
    ciudad      = models.CharField(max_length=100, blank=True, null=True)
    dia         = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    gravedad    = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

    def gravedad_de_consulta(self):
        print('Hola')
        qs = self.respuesta_set.all()
        print(qs)
        promedio = self.respuesta_set.all().aggregate(Avg('titulo_binario'))
        print(promedio)
        valor_promedio = promedio['titulo_binario__avg']
        if valor_promedio < 0.3:
            self.gravedad = 'Baja'
        elif valor_promedio > 0.3 and valor_promedio < 0.6:
            self.gravedad = 'Media'
        elif valor_promedio > 0.6:
            self.gravedad = 'Alta'
        print(valor_promedio)
        self.save()
        return valor_promedio

def consulta_post_save(instance, sender, created, *args, **kwargs):
    if instance.ciudad is not None:
        ciudad = instance.ciudad
        qs = Ciudad.objects.filter(nombre__icontains=ciudad)
        if qs.exists():
            pass
        else:
            Ciudad.objects.create(nombre=instance.ciudad)

post_save.connect(consulta_post_save, sender=Consulta)

class Ciudad(models.Model):
    nombre  = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk)

ESTADO_CODIGO = (
    ('Activo', 'Activo'),
    ('Usado', 'Usado'),
    ('Cancelado', 'Cancelado')
)

class Validacion(models.Model):
    telefono    = models.CharField(max_length=10)
    codigo      = models.IntegerField()
    estado      = models.CharField(max_length=30, choices=ESTADO_CODIGO)

    def __str__(self):
        return str(self.pk)
