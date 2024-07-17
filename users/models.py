from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=50, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    verification_code = models.CharField(max_length=9, verbose_name='Код верификации', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    def block_user(self):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
