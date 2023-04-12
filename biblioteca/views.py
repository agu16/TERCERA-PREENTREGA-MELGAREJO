from django.shortcuts import render
from .models import Libros
from django.shortcuts import redirect
from .models import Libros

# Create your views here.

def plantilla_hija(request):
    return render (request , "plantilla_hija.html", {})

def crear_libro(request):
    if request.method == "POST":
        objeto = Libros(
        nombre = request.POST["nombre"],
        genero = request.POST["genero"],
        autor = request.POST["autor"],
        editorial =  request.POST["editorial"],
        )
        objeto.save() 
        return redirect ('detalle_objeto', pk=objeto.pk)
    else:
        return render(request, 'crear_libro.html')
    
def buscar_libro(request):
    if request.method == "POST":
         valor_buscado = request.POST['valor_buscado']
         objeto = get_object_or_404 ( buscar_libro, campo_busqueda=valor_buscado) 
    