from django.shortcuts import render
from .models import Libros
from django.shortcuts import redirect
from .models import Libros
from .forms import SeleccionLibroFormulario
from .models import Libros

# Create your views here.

def plantilla_hija(request):
    return render (request , "plantilla_hija.html", {})

def crear_libro(request):
    if request.method == "POST":
        form = SeleccionLibroFormulario(request.POST)
        if form.is_valid():
            libro = form.save()  # Guardar el formulario en la base de datos
            return redirect('detalle_objeto', pk=libro.pk)
    else:
        form = SeleccionLibroFormulario()
    return render(request, 'crear_libro.html', {'form': form})



def buscar_libro(request):
     if request.method == 'POST':
         valor_buscado = request.POST['valor_buscado']
         Libros , campo_busqueda = valor_buscado
         return render(request, 'detalle_objeto.html', {'objeto': objeto})
     else:
          return render(request, 'formulario_buscar_libro.html')
    

    