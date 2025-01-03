from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'description']

@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'category', 'description']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'description', 'price', 'stock', 'category', 'subcategory', 'is_available']
  
  