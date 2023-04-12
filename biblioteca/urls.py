
from django.urls import path
from biblioteca import views
from .views import crear_libro
from .views import buscar_libro

app_name = "biblioteca"

urlpatterns = [
    path("plantilla_hija/" , views.plantilla_hija),
    path ("crear_libro/" , crear_libro , name = "crear_libro"),
    path ("buscar_libro/" , buscar_libro , name = "buscar_libro" ),
    ]
