"""menudigitalqr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets, generics, status
from rest_framework.views import APIView
from product.models import Product
from django.conf import settings
from rest_framework.response import Response

from django.conf.urls.static import static


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    
    
class RestaurantViewset(APIView):
    serializer_class = ProductSerializer

    def get(self, request, author_id):

    
        queryset = Product.objects.get(author_id = author_id)
        product  = ProductSerializer(queryset)
        self.data = product.data
        
        
        if queryset is None:
            self.error = "datas are not found"
            return Response(self.error, status=status.HTTP_404_NOT_FOUND)
                
        else:
            return Response(self.data, status=status.HTTP_200_OK)
        pass
            
        # author_id = self.request.query_params.get('author_id')

        
router = routers.DefaultRouter()
router.register(r'product', ProductsViewSet)

    
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path(r'menu/<int:author_id>', RestaurantViewset.as_view(), name='Restaurant') 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)