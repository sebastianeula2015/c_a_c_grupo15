from django import forms
from django.core.exceptions import ValidationError

class ProductoNuevoForm(forms.Form):
    descripcion = forms.CharField(label="Descripcion", required=True, max_length=200,  widget=forms.TextInput(attrs={'class': "form-control"})) 
    codigo = forms.IntegerField(label="Codigo", required=True,  widget=forms.NumberInput(attrs={'class': "form-control"})) 
    cantidades = forms.IntegerField(label="Cantidades", required=True,  widget=forms.NumberInput(attrs={'class': "form-control"}))
    precio_unidad = forms.DecimalField(label="Precio Unidad", required=True,  widget=forms.NumberInput(attrs={'class': "form-control"}))
    
    def clean_nombre(self):
        if not self.cleaned_data["codigo"].isalpha():
            raise ValidationError("Error en el campo codigo")
        
        return self.cleaned_data["codigo"]
    

class ProductoModificacionForm(forms.Form):
    descripcion = forms.CharField(label="Descripcion", required=True, max_length=200,  widget=forms.TextInput(attrs={'class': "form-control"})) 
    codigo = forms.IntegerField(label="Codigo", required=True,  widget=forms.NumberInput(attrs={'class': "form-control"})) 
    cantidades = forms.IntegerField(label="Cantidades", required=True,  widget=forms.NumberInput(attrs={'class': "form-control"}))
    precio_unidad = forms.DecimalField(label="Precio Unidad", required=True,  widget=forms.NumberInput(attrs={'class': "form-control"}))
    
    def clean_nombre(self):
        if not self.cleaned_data["codigo"].isalpha():
            raise ValidationError("Error en el campo codigo")
        
        return self.cleaned_data["codigo"]