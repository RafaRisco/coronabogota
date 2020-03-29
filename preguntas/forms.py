from django import forms

from .models import Respuesta

TITULO_OPCIONES = (
    ('Si', 'Si'),
    ('No', 'No')
)

class RespuestaForm(forms.Form):
    titulo = forms.ChoiceField(choices=TITULO_OPCIONES, widget=forms.RadioSelect())
