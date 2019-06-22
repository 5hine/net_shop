from django.contrib import admin
from .models import ProductCategory, Product
# Register your models here.


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'category', 'price', 'reserve', 'is_on_shelf', 'add_time']
    list_editable = ['name', 'price', 'reserve']
    list_per_page = 5


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
