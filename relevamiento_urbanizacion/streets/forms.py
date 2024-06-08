from django import forms
from .models import Street

class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ['name', 'start_number', 'end_number']