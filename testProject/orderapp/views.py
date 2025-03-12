from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ViewSet
from userapp import permissions
from .service import create
# Create your views here.
class OrderView(ViewSet):
    permission_classes = [permissions.IsAuthorizeUser]


    @swagger_auto_schema(
        operation_description="Создать заказ",
        responses={200: openapi.Response("Успешный ответ")},
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
    def create(self, request):
        return create(request)
