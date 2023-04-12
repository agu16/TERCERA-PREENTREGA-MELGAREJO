from django.db import models

# Create your models here.

class Libros (models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    autor =  models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
