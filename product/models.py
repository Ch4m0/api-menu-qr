from django.db import models

# Create your models heroe
class Product(models.Model):
    nombre = models.CharField(max_length= 200)
    descripcion = models.TextField(null=True)
    precio = models.TextField(null=True)
    foto_producto = models.ImageField(null=True)
    
    
