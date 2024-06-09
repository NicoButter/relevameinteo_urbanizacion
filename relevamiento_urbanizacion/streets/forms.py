from django import forms
from .models import Street

class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ['es_avenida', 'nombre', 'altura_inicial', 'altura_final', 'coordenadas_iniciales', 'coordenadas_finales']
        
        def save(self, commit=True):
            street = super().save(commit=False)
            street.longitud_en_metros = street.altura_final / 100 if street.altura_final else 0
            if commit:
                street.save()
            return street
