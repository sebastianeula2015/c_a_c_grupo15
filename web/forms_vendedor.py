from django import forms
from django.core.exceptions import ValidationError

class VendedorNuevoForm(forms.Form):
    nombres = forms.CharField(label="Nombres", required=True, max_length=60,  widget=forms.TextInput(attrs={'class': "form-control"})) 

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("Error en el campo nombre")
        
        return self.cleaned_data["nombre"]
    

class VendedorModificacionForm(forms.Form):
    nombres = forms.CharField(label="Nombres", required=True, max_length=60,  widget=forms.TextInput(attrs={'class': "form-control"}))     
    
    def clean_nombre(self):
        
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("Error en el campo nombre")
        
        return self.cleaned_data["nombres"]
    