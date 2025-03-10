from django.http import request
from rest_framework.response import Response

from ..models.Product import Product
from ..filters.ProductsFilter import ProductsFilter
from ..serializer.ProductSerializer import ProductSerializer

def getProducts(request):
    products = Product.objects.all()
    product_filter = ProductsFilter(request.data, queryset=products)
    filtered_products = product_filter.qs
    serializer = ProductSerializer(filtered_products, many=True)
    return Response(serializer.data)
