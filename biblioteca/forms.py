from django import forms

class SeleccionLibroFormulario(forms.Form ):
    nombre = forms.forms.CharField( max_length= 40)
    autor = forms.forms.forms.CharField( max_length=20)
    
    