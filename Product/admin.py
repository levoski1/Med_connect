from django.contrib import admin
from Product.models import ProductModel



class ProductAdmin(admin.ModelAdmin):
    search_fields = ['product_name']

    
admin.site.register(ProductModel, ProductAdmin)
