
from django.urls import path
from biblioteca import views
from .views import crear_libro

app_name = "biblioteca"

urlpatterns = [
    path("plantilla_hija/" , views.plantilla_hija),
    path ("crear_libro/" , crear_libro , name = "crear_libro"),
    ]
