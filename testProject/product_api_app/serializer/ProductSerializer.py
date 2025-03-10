from rest_framework import serializers

from ..models import Product
from ..models import Category
from .CategorySerializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'specifications', 'category']

    def create(self, validated_data):

        category_data = validated_data.pop('category')
        category, created = Category.objects.get_or_create(**category_data)
        product = Product.objects.create(category=category, **validated_data)

        return product