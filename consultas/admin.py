from django.contrib import admin

# Register your models here.
from .models import Consulta, Ciudad, Validacion

class ConsultaAdmin(admin.ModelAdmin):
    list_display = [
        'telefono',
        'gravedad',
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
