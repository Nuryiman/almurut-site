# Generated by Django 5.1.1 on 2024-09-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.IntegerField(null=True),
        ),
    ]
