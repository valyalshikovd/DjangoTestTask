from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import permission_classes, action
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from ..service.category_service import get_categories
from ..service.category_service import create_category
from userapp import permissions
from ..serializer import CategorySerializer


class CategoryView(ViewSet):

    @swagger_auto_schema(
        operation_description="Получить категории",
        responses={200: openapi.Response("Успешный ответ")})
    def list(self, request):
        return get_categories(request)


    @swagger_auto_schema(
        operation_description="Создать категорию",
        request_body= CategorySerializer.CategorySerializer,
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
    @action(detail=False, permission_classes=[permissions.permissions.IsAdminUser], methods=['post'])
    def post(self, request):
        return create_category(request)
