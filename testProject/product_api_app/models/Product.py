from django.db import models
from .Category import Category

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    price = models.FloatField(verbose_name="Цена")
    image = models.TextField(max_length=255, verbose_name="Картинка", null=True)
    specifications = models.TextField(verbose_name="Характеристики", blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
