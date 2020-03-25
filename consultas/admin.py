from django.contrib import admin

# Register your models here.
from .models import Consulta, Ciudad

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
