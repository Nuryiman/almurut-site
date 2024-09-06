from django.contrib import admin
from django.utils.html import format_html

from market.models import Product, ProductGallery, ProductCategory


class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 4  # Количество пустых форм для добавления новых записей


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'sales_percent', 'image_tag',]
    search_fields = ['name', 'description']
    inlines = [ProductGalleryInline]  # Включаем галерею товаров как inline

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100px"/>'.format(obj.preview_image.url))

    image_tag.short_description = 'превью-изображения'


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']
    search_fields = ['product__name']
