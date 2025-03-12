from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from ..service.products_service import getProducts

class ProductsView(ViewSet):

    @swagger_auto_schema(
        operation_description="Выбрать товары соответствующей категории",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'category_name': openapi.Schema(type=openapi.TYPE_STRING, description="Имя категории"),
            },
        ),
        responses={200: openapi.Response("Успешный ответ")},
    )
    @action(detail=False, methods=['post'])
    def getProducts(self, request):
        return getProducts(request)
