from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


TELEPHONE_REGEX = '^[0-9]*$'

def min_length(value):
    if len(value) < 10:
        raise ValidationError('Debe tener al menos 6 carácteres')

class TelefonoForm(forms.Form):
    telefono    = forms.CharField(
                        max_length=10,
                        validators=[
                        RegexValidator(regex=TELEPHONE_REGEX, message='introduce solo números y que sean 9 dígitos, sin puntos ni dígito de verificación'),
                        min_length],
                        widget=forms.TextInput(attrs={"class": 'form-control form-control-lg'})
                        )
