from django import forms
from django.core.exceptions import ValidationError
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre del producto'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese una descripcion'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("Error en el campo nombre")
        return self.cleaned_data["nombre"]

