from django.contrib import admin

# Register your models here.
from .models import Consulta, Ciudad, Validacion, Persona

class ConsultaAdmin(admin.ModelAdmin):
    list_display = [
        'telefono',
        'gravedad',
        'ciudadano',
        'lat',
        'long',
        'address',
        'ciudad',
        'dia'
    ]

admin.site.register(Consulta, ConsultaAdmin)

class CiudadAmin(admin.ModelAdmin):
    list_display = [
        'nombre'
    ]

admin.site.register(Ciudad, CiudadAmin)

class ValidacionAdmin(admin.ModelAdmin):
    list_display = [
        'telefono',
        'codigo',
        'estado'
    ]

admin.site.register(Validacion, ValidacionAdmin)

class PersonaAdmin(admin.ModelAdmin):
    list_display = [
        'nombre_y_apellidos',
        'dia_nacimiento',
        'mes_nacimiento',
        'año_nacimiento',
        'cedula',
        'sexo',
        'direccion'
    ]

admin.site.register(Persona, PersonaAdmin)
