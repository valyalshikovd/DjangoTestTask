from rest_framework import serializers

from cartapp.models import CartItem, Cart
from product_api_app.serializer.ProductSerializer import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(source='cartitem_set', many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'products']
