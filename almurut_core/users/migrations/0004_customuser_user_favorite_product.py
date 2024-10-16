# Generated by Django 5.1 on 2024-10-02 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_remove_product_user_favorite_product'),
        ('users', '0003_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_favorite_product',
            field=models.ManyToManyField(null=True, related_name='favorite_products', to='market.product'),
        ),
    ]
