import base64
from io import BytesIO
from django.core.files import File

from django.http import request
from rest_framework.response import Response

from ..models.Product import Product
from ..filters.ProductsFilter import ProductsFilter
from ..serializer.ProductSerializer import ProductSerializer
from .object_storage_service import get_file


def getProducts(request):
    products = Product.objects.all()
    product_filter = ProductsFilter(request.data, queryset=products)
    filtered_products = product_filter.qs

    for product in filtered_products:
        injectFilesToJson(product)

    serializer = ProductSerializer(filtered_products, many=True)
    return Response(serializer.data)

def injectFilesToJson(product: Product):
    image_path = product.image
    file_content = get_file("fittintest", image_path)['Body'].read()
    image_base64 = base64.b64encode(file_content).decode('utf-8')
    product.image = image_base64