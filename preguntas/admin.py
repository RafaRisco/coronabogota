from django.contrib import admin

from .models import Pregunta, Respuesta

# Register your models here.

class PreguntaAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'titulo'
    ]


admin.site.register(Pregunta, PreguntaAdmin)

class RespuestaAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'titulo',
        'titulo_pregunta',
        'titulo_binario',
        'consulta',
        'numero_consulta',
    ]

admin.site.register(Respuesta, RespuestaAdmin)
