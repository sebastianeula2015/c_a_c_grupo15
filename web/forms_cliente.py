from django import forms
from django.core.exceptions import ValidationError
#from .models import Post


class ClienteNuevoForm(forms.Form):

    nombres = forms.CharField(label="Nombres", required=True,  widget=forms.TextInput(attrs={'class': "form-control ",'placeholder': 'ingrese su nombre'}))  
    dni = forms.IntegerField(label="DNI", required=True,  widget=forms.NumberInput(attrs={'class': "form-control"})) 
    email = forms.EmailField(label="Email", required=True , widget=forms.EmailInput(attrs={'class': "form-control"})) 
    telefono = forms.CharField(label="Telefono", required=True, widget=forms.TextInput(attrs={'class': "form-control"})) 
    direccion = forms.CharField(label="Direccion", required=True, widget=forms.TextInput(attrs={'class': "form-control"})) 

    def clean_nombre(self):
        if not self.cleaned_data["nombres"].isalpha():
            raise ValidationError("Error en el campo nombre")
        
        return self.cleaned_data["nombres"]


class ClienteModificacionForm(forms.Form):
    nombres = forms.CharField(label="Nombres", required=True,  widget=forms.TextInput(attrs={'class': "form-control ",'placeholder': 'ingrese su nombre'}))  
    dni = forms.IntegerField(label="DNI", required=True,  widget=forms.NumberInput(attrs={'class': "form-control"})) 
    email = forms.EmailField(label="Email", required=True , widget=forms.EmailInput(attrs={'class': "form-control"})) 
    telefono = forms.CharField(label="Telefono", required=True, widget=forms.TextInput(attrs={'class': "form-control"})) 
    direccion = forms.CharField(label="Direccion", required=True, widget=forms.TextInput(attrs={'class': "form-control"})) 

    def clean_nombre(self):
        if not self.cleaned_data["nombres"].isalpha():
            raise ValidationError("Error en el campo nombre")
        
        return self.cleaned_data["nombres"]
    