from django import forms
from django.core.exceptions import ValidationError

class AltaAlumnoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True) 
    apellido = forms.CharField(label="Apellido", required=True) 
    dni = forms.IntegerField(label="DNI", required=True)
    email = forms.EmailField(label="email", required=True)
    direccion = forms.CharField(label="Direccion", required=True) 

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("Error en el campo nombre")
        
        return self.cleaned_data["nombre"]
    

    #def clean(self):
    #    if self.cleaned_data["nombre"] == "carlos":
    #        raise ValidationError("existe")
        
    #    return self.cleaned_data