from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from cartapp.models import Cart, CartItem
from cartapp.serializers import CartSerializer
from product_api_app.models import Product


def getCart(request):
    username = request.user
    user = get_object_or_404(User, username=username)
    cart, _ = Cart.objects.get_or_create(user=user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


def create(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return Response({'message': 'Cart created' if created else 'Cart already exists'}, status=status.HTTP_201_CREATED)


def update(request):
    cart = get_object_or_404(Cart, user=request.user)
    product_name = request.data.get('product_name')
    quantity = int(
        request.data.get('quantity', 1))
    product = get_object_or_404(Product, name=product_name)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += quantity
    cart_item.save()
    return Response({'message': 'Cart updated'})


def delete_item(request):
    cart = get_object_or_404(Cart, user=request.user)
    product_name = request.data.get('product_name')
    product = get_object_or_404(Product, name=product_name)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()
    return Response({'message': 'Cart item removed from cart'})
