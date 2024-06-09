from django.contrib import admin
from django import forms
from .models import CustomUser, PhoneNumber

# Define custom forms if necessary
class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = '__all__'  # O especifica los campos que deseas mostrar en el formulario

# Register your models with custom admin forms
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Optionally define list_display, list_filter, search_fields, etc.
    pass

@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    # Optionally define list_display, list_filter, search_fields, etc.
    form = PhoneNumberForm
