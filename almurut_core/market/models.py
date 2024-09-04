from django.core.validators import MaxValueValidator
from django.db import models


class ProductCategory(models.Model):
    """Моделька категории для товара"""

    name = models.CharField(
        max_length=100,
        verbose_name='Название категории'
    )

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    """Моделька для товаров"""
    name = models.CharField(max_length=150, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.PositiveIntegerField(verbose_name='Цена товара')
    preview_image = models.ImageField(verbose_name='Изображение товара')
    sales_percent = models.PositiveIntegerField(
        verbose_name='Скидка в процентах',
        null=True,
        validators=[MaxValueValidator(100)]
    )
    new_expiry_date = models.DateField(verbose_name='Дата истечения срока действия')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductGallery(models.Model):
    """Моделька для галереи товаров"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    image = models.ImageField(verbose_name='Изображение')

    class Meta:
        verbose_name = 'Галерея товара'
        verbose_name_plural = 'Галереи товаров'
