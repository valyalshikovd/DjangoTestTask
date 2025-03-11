from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from userapp import permissions
from .service import getCart
from .service import create
from .service import update
from .service import delete_item

# Create your views here.


class CartView(ViewSet):
    permission_classes = [permissions.IsAuthorizeUser]

    def list(self, request):
        return getCart(request)

    def create(self, request):
        return create(request)

    @action(detail=False, methods=['put'])
    def put(self, request):
        return update(request)

    @action(detail=False, methods=['delete'])
    def delete(self, request):
        return delete_item(request)

