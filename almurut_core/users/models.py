from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """Модель для пользователей"""

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        unique=True,
        db_index=True
    )
    avatar = models.ImageField(null=True)
    birth_day = models.DateField(
        null=True,
        blank=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        unique_together = ('first_name', 'last_name')


# class User(models.Model):
#     """Модель для пользователей"""
#
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#
#     email = models.EmailField(unique=True)
#     password = models.TextField()
#
#     phone_number = models.CharField(
#         max_length=25,
#         null=True,
#         blank=True,
#     )
#     address = models.TextField()
#     avatar = models.IntegerField()
#
#     is_superuser = models.BooleanField()    # является ли пользователь администратором
#     is_staff = models.BooleanField()    # является ли пользователь администратором
#
#     birth_day = models.DateField(null=True, blank=True)
#     date_joined_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"
#         unique_together = ('first_name', 'last_name')
