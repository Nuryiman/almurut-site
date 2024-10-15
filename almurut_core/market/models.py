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

    def __str__(self):
        return self.name


class Product(models.Model):
    """Моделька для товаров"""

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.PositiveIntegerField(verbose_name='Цена товара', help_text='в сомах')
    sales_percent = models.PositiveIntegerField(
        verbose_name='Скидка в процентах',
        null=True,
        validators=[MaxValueValidator(100)]
    )
    preview_image = models.ImageField(verbose_name='Изображение товара', upload_to='product_previews_images/')

    new_expiry_date = models.DateField(verbose_name='Дата истечения отметки Новый')

    def get_price_with_sales(self):
        """Возвращает цену с учетом скидки"""
        if self.sales_percent == 0:
            return self.price
        return int((self.price / 100) * (100 - self.sales_percent))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductGallery(models.Model):
    """Моделька для галереи товаров"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='product_gallery')
    image = models.ImageField(verbose_name='Изображение', upload_to='product_gallery')

    class Meta:
        verbose_name = 'Галерея товара'
        verbose_name_plural = 'Галереи товаров'


class ProductUserRating(models.Model):
    from users.models import CustomUser
    """Моделька для рейтинга продуктов"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    phone = models.PositiveSmallIntegerField(null=True)
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MaxValueValidator(1)])
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ('product', 'user',)


# class UserFavoriteProduct(models.Model):
#     """Моделька для избранных продуктов пользователей"""
#     from users.models import CustomUser
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
#
#     class Meta:
#         verbose_name = 'Избранный продукт'
#         verbose_name_plural = 'Избранные продукты'
#         unique_together = ('user', 'product',)
