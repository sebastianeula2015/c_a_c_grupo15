from django import forms
from django.core.exceptions import ValidationError
from .models import Venta, DetalleVenta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'vendedores': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'detalle_venta': forms.Select(attrs={'class': 'form-control'}),
        }

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = '__all__'
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }