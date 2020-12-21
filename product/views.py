from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, generics, status
from rest_framework.response import Response

from .models import Category, Product
from rest_framework.views import APIView

# Create your views here.
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(APIView):
    serializer_class = CategorySerializer     
    
    def get(self, request, author_id):
    
        queryset = Category.objects.filter(author_id = author_id)
        
        categoria  = CategorySerializer(queryset, many=True)
        
        self.data = categoria.data
        
        if queryset is None:
            self.error = "datas are not found"
            return Response(self.error, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(self.data, status=status.HTTP_200_OK)
        pass
            

