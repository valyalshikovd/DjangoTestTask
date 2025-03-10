import json
import os
import uuid

from rest_framework import status
from rest_framework.response import Response

from ..models.Product import Product
from ..serializer.ProductSerializer import ProductSerializer
from ..filters.ProductFilter import ProductFilter
from ..service.object_storage_service import upload_file
from .products_service import injectFilesToJson


def get_products(request):
    products = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=products)
    filtered_products = product_filter.qs
    for product in filtered_products:
        injectFilesToJson(product)

    serializer = ProductSerializer(filtered_products, many=True)
    return Response(serializer.data)

def create_product(request):
    serializer = ProductSerializer(data=json.loads(dict(request.data).get('params')[0]))
    image = request.FILES['image']

    file_name = str(uuid.uuid4()) + os.path.splitext(image.name)[1]
    upload_file('fittintest', file_name, image)

    if serializer.is_valid():
        serializer.save(image=file_name)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
