from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from ..service.product_service import get_products
from ..service.product_service import create_product
from userapp import permissions


class ProductListView(ViewSet):

    def list(self, request):
        return get_products(request)

    @action(detail=False, permission_classes=[permissions.IsAdmin], methods=['post'])
    def post(self, request):
        return create_product(request)
