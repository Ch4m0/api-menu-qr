from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from product.models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = '__all__'
 

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many = True, read_only=True, source='product_set')
    
    class Meta: 
        model = Category
        fields = '__all__'
