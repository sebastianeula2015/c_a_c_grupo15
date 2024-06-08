from django import forms
from django.core.exceptions import ValidationError
from .models import Vendedor

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su email'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su teléfono'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su DNI'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su provincia'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su dirección'}),
            'nro_vendedor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nro de vendedor'}),
        }
    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("Error en el campo nombre")
        return self.cleaned_data["nombre"]

    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("Error en el campo apellido")
        return self.cleaned_data["apellido"]

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if Vendedor.objects.filter(dni=dni).exists():
            raise forms.ValidationError("Ya existe un cliente con este DNI.")
        return dni

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Vendedor.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un cliente con este email.")
        return email
    