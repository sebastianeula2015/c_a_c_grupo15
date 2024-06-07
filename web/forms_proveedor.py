from django import forms
from django.core.exceptions import ValidationError
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el email'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'}),
            'cuit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el CUIT'}),
        }
        error_messages = {
            'email': {
                'invalid': "Por favor, introduce una dirección de correo electrónico válida.",
                'unique': "Ya existe un proveedor con este email.",
            },
        }