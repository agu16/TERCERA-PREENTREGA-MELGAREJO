from django.shortcuts import render
from .models import Libros
from django.shortcuts import redirect
from .models import Libros
from .forms import SeleccionLibroFormulario

# Create your views here.

def plantilla_hija(request):
    return render (request , "plantilla_hija.html", {})

def crear_libro(request):
     if request.method == "POST":
        form = SeleccionLibroFormulario(request.POST)
        if form.is_valid():
            objeto = form.save()
            return redirect('detalle_objeto', pk=objeto.pk)
     else:
        form = SeleccionLibroFormulario()
     return render(request, 'crear_libro.html', {'form': form})
    

    