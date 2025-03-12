import django_filters
from ..models.Product import Product


class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="priceMin", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="priceMax", lookup_expr="lte")
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['price_min', 'price_max', 'name']