from django import forms
from django.core.exceptions import ValidationError
from .models import Venta, DetalleVenta, Producto
from django.forms import inlineformset_factory

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['fecha', 'cliente', 'vendedores']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'vendedores': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'precio', 'precio_total']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control','type': 'number', 'min': 0}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'precio_total': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['precio_total'].initial = ''

    def clean(self):
        cleaned_data = super().clean()
        precio = cleaned_data.get('precio')
        cantidad = cleaned_data.get('cantidad')

        if precio is None or cantidad is None:
            self.add_error('precio', 'Precio y cantidad son campos requeridos')
            self.add_error('cantidad', 'Precio y cantidad son campos requeridos')

        return cleaned_data
    
DetalleVentaFormSet = inlineformset_factory(
    Venta,
    DetalleVenta,
    form=DetalleVentaForm,
    extra=5,  # Puedes ajustar según la cantidad inicial de formularios
    can_delete=False,
)