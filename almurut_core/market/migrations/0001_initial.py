# Generated by Django 5.1 on 2024-09-25 11:02

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('price', models.PositiveIntegerField(help_text='в сомах', verbose_name='Цена товара')),
                ('sales_percent', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Скидка в процентах')),
                ('preview_image', models.ImageField(upload_to='product_previews_images/', verbose_name='Изображение товара')),
                ('new_expiry_date', models.DateField(verbose_name='Дата истечения отметки Новый')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.productcategory')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_gallery', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Галерея товара',
                'verbose_name_plural': 'Галереи товаров',
            },
        ),
        migrations.CreateModel(
            name='ProductUserRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.PositiveSmallIntegerField(null=True)),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MaxValueValidator(1)])),
                ('comment', models.TextField(null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('product', 'user')},
            },
        ),
    ]
