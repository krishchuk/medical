from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Procedure(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    picture = models.ImageField(upload_to='procedure/', verbose_name='изображение', **NULLABLE)
    price = models.IntegerField(verbose_name='цена')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'процедура'
        verbose_name_plural = 'процедуры'
