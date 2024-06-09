from django import forms
from .models import Street

class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ['es_avenida', 'nombre', 'altura_inicial', 'altura_final', 'coordenadas_iniciales', 'coordenadas_finales']
