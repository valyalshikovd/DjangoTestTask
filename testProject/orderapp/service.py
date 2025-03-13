from cartapp.models import Cart
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from .models import Order, OrderItem

def create(request):
    username = request.user
    user = get_object_or_404(User, username=username)
    cart, _ = Cart.objects.get_or_create(user=user)
    return create_order(cart)


def create_order(cart):
    order = Order.objects.create(user=cart.user)

    for cart_item in cart.cartitem_set.all():
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity
        )
    cart.products.clear()
    return Response({'message': 'Order created' }, status=status.HTTP_201_CREATED)
