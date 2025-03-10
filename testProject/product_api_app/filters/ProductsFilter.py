import django_filters
from django_filters import filters

from ..models.Product import Product

class ProductsFilter(django_filters.FilterSet):
    category = filters.CharFilter(field_name="category__name", lookup_expr="iexact")

    class Meta:
        model = Product
        fields = ['category']