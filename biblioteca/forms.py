from django import forms

class SeleccionLibroFormulario(forms.Form ):
    nombre = forms.CharField( max_length= 40)
    genero = forms.CharField( max_length= 40)
    autor = forms.CharField( max_length= 40)
    editorial = forms.CharField( max_length= 40)
    
    