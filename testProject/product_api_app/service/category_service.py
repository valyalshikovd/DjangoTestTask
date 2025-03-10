from rest_framework import status
from rest_framework.response import Response

from ..serializer.CategorySerializer import CategorySerializer
from ..models.Category import Category

def get_categories(request):
    products = Category.objects.all()
    serializer = CategorySerializer(products, many=True)
    return Response(serializer.data)

def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
