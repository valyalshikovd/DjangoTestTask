from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.ProductView import ProductListView
from .views.ProductsView import ProductsView
from .views.CategoryView import CategoryView


router = DefaultRouter()
router.register(r'product', ProductListView, basename='product-list')
router.register(r'product/', ProductsView, basename='products'),
router.register(r'category', CategoryView, basename='category')


urlpatterns = router.urls

