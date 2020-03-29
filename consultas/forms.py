from django import forms

from .models import Persona

SEXO_OPCIONES = (
    ('Hombre', 'Hombre'),
    ('Mujer', 'Mujer')
)

class PersonaForm(forms.ModelForm):
    sexo = forms.ChoiceField(choices=SEXO_OPCIONES, widget=forms.RadioSelect())

    class Meta:
        model = Persona
        fields = [
            'nombre_y_apellidos',
            'dia_nacimiento',
            'mes_nacimiento',
            'año_nacimiento',
            'cedula',
            'direccion'
        ]
        widgets = {
            'nombre_y_apellidos': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder': 'Jose Fernandez'}),
            'direccion': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder': 'Calle 61, # 28'}),
            'dia_nacimiento': forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': '1'}),
            'mes_nacimiento': forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': '1'}),
            'año_nacimiento': forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': '1975'}),
            'cedula': forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': '11111111'}),
        }
