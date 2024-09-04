from django.contrib import admin
from market.models import Product, ProductGallery, ProductCategory


class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1  # Количество пустых форм для добавления новых записей


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'sales_percent']
    search_fields = ['name', 'description']
    inlines = [ProductGalleryInline]  # Включаем галерею товаров как inline


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']
    search_fields = ['product__name']
