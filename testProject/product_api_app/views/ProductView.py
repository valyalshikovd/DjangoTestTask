from rest_framework.decorators import action
from rest_framework.views import APIView

from ..service.product_service import get_products
from ..service.product_service import create_product
from userapp import permissions


class ProductListView(APIView):
    def get(self, request):
        return get_products(request)

    @action(detail=False, permission_classes=[permissions.IsAdmin])
    def post(self, request):
        return create_product(request)
