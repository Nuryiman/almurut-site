# Generated by Django 5.1 on 2024-10-15 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_userfavoriteproduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFavoriteProduct',
        ),
    ]
