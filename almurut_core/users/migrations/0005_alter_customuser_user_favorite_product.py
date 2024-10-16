# Generated by Django 5.1 on 2024-10-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_userfavoriteproduct'),
        ('users', '0004_customuser_user_favorite_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_favorite_product',
            field=models.ManyToManyField(related_name='favorite_products', to='market.product'),
        ),
    ]
