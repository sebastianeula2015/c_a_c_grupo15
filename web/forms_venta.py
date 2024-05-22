from django import forms
from django.core.exceptions import ValidationError

class VentaNuevaForm(forms.Form):
    fechaVenta = forms.DateField(label="Fecha", required=True,  widget=forms.DateInput(attrs={'class': "form-control ",'placeholder': 'ingrese su nombre'}))  
    horaVenta = forms.TimeField(label="Hora", required=True,  widget=forms.TimeInput(attrs={'class': "form-control"})) 
    clienteId = forms.IntegerField(label="Cliente", required=True , widget=forms.NumberInput(attrs={'class': "form-control"})) 
    vendedorId = forms.IntegerField(label="Vendedor", required=True, widget=forms.NumberInput(attrs={'class': "form-control"})) 
    totalVenta = forms.DecimalField(label="Total Venta", required=True, widget=forms.NumberInput(attrs={'class': "form-control"})) 


    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("Error en el campo nombre")
        
        return self.cleaned_data["nombre"]
    

class VentaModificicacionForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True) 
    apellido = forms.CharField(label="Apellido", required=True) 
    dni = forms.IntegerField(label="DNI", required=True)
    email = forms.EmailField(label="email", required=True)
    direccion = forms.CharField(label="Direccion", required=True) 

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("Error en el campo nombre")
        
        return self.cleaned_data["nombre"]
    