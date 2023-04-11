from django.db import models

# Create your models here.

class Libros (models.Model):
    nombre = models.CharField(max_length=40)
    edicion = models.IntegerField()
    autor =  models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
