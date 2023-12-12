from django.db import models

class Producto_Proteccion(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    cantidad = models.PositiveBigIntegerField()
    imagen = models.ImageField()

class Producto_almacen(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    cantidad = models.PositiveBigIntegerField()
    imagen = models.ImageField()
    

