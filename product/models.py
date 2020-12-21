from django.db import models
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.
class Category(models.Model):
    nombre = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nombre
    

# Create your models heroe
class Product(models.Model):
    nombre = models.CharField(max_length = 200)
    descripcion = models.TextField(null = True)
    precio = models.TextField(null = True)
    foto_producto = models.ImageField(null = True)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.foto_producto))

    image_tag.short_description = 'Imagen' 
    
    def __str__(self):
        return self.nombre