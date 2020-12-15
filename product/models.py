from django.db import models
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import User

# Create your models heroe
class Product(models.Model):
    nombre = models.CharField(max_length= 200)
    descripcion = models.TextField(null=True)
    precio = models.TextField(null=True)
    foto_producto = models.ImageField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    
