from django.contrib import admin

# Register your models here.
from .models import Consulta

class ConsultaAdmin(admin.ModelAdmin):
    list_display = [
        'telefono',
        'lat',
        'long',
        'address',
        'dia'
    ]

admin.site.register(Consulta, ConsultaAdmin)
