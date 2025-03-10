from django.contrib import admin

from .models.Product import Product
from .models.Category import Category

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)