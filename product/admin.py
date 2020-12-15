from django.contrib import admin
from .models import Product

#Register your models here.
class YourModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(author=request.user)


class ProductAdmin(admin.ModelAdmin):
    # you should prevent author field to be manipulated 
    readonly_fields = ['author']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(author=request.user)

    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
        Product.author = request.user
        return super().get_form(request, obj, **kwargs)


    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.author_id = request.user.id
        obj.last_modified_by = request.user
        obj.save()

admin.site.register(Product, ProductAdmin)