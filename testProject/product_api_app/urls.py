from django.contrib import admin
from django.urls import path

from .views.ProductView import ProductListView
from .views.ProductsView import ProductsView
from .views.CategoryView import CategoryView

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product-list'),
    path('products/', ProductsView.as_view(), name='products'),
    path('category/', CategoryView.as_view(), name='category')
]