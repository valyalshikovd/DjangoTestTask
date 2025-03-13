from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from ..service.product_service import get_products
from ..service.product_service import create_product
from userapp import permissions
from ..serializer.ProductSerializer import ProductSerializer

class ProductListView(ViewSet):

    @swagger_auto_schema(
        operation_description="Получить товары и отфильтровать по цене",
        responses={200: openapi.Response("Успешный ответ")},
        manual_parameters=[
            openapi.Parameter(
                name="priceMin",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Минимальная цена",
                required=True
            ),
            openapi.Parameter(
                name="priceMax",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Максимальная цена",
                required=False
            )
        ],
    )
    def list(self, request):
        return get_products(request)

    @swagger_auto_schema(
        operation_description="Добавить товар",
        request_body=ProductSerializer,
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
    @action(detail=False, permission_classes=[permissions.IsAdmin], methods=['post'])
    def post(self, request):
        return create_product(request)
