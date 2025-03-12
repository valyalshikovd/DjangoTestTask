from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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

    @swagger_auto_schema(
        operation_description="Получить корзину пользователя. Если корзины нет она создается",
        responses={200: openapi.Response("Успешный ответ"), 404: openapi.Response("Пользователь не существует")},
        manual_parameters=[
            openapi.Parameter(
                name="Authorization",
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description="JWT токен. Формат: Bearer <token>",
                required=True
            )
        ]
    )
    def list(self, request):
        return getCart(request)

    @swagger_auto_schema(
        operation_description="Создать корзину",
        responses={200: openapi.Response("Успешный ответ"), 404: openapi.Response("Пользователь не существует")},
        manual_parameters=[
            openapi.Parameter(
                name="Authorization",
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description="JWT токен. Формат: Bearer <token>",
                required=True
            )
        ]
    )
    def create(self, request):
        return create(request)

    @swagger_auto_schema(
        operation_description="Добавить товар в коррзину",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'product_name': openapi.Schema(type=openapi.TYPE_STRING, description="Имя продукта"),
                'quantity': openapi.Schema(type=openapi.TYPE_STRING, description="колисество товара"),
            },
        ),
        responses={200: openapi.Response("Успешный ответ"), 404: openapi.Response("Пользователя или товара не существует")},
        manual_parameters=[
            openapi.Parameter(
                name="Authorization",
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description="JWT токен. Формат: Bearer <token>",
                required=True
            ),
        ]
    )
    @action(detail=False, methods=['put'])
    def put(self, request):
        return update(request)

    @swagger_auto_schema(
        operation_description="Удалить товар из корзины",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'product_name': openapi.Schema(type=openapi.TYPE_STRING, description="Имя продукта"),
            },
        ),
        responses={200: openapi.Response("Успешный ответ"), 404: openapi.Response("Пользователь не существует")},
        manual_parameters=[
            openapi.Parameter(
                name="Authorization",
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description="JWT токен. Формат: Bearer <token>",
                required=True
            ),

        ]
    )
    @action(detail=False, methods=['delete'])
    def delete(self, request):
        return delete_item(request)

