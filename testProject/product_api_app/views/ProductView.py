
from rest_framework.views import APIView

from ..service.product_service import get_products
from ..service.product_service import create_product

class ProductListView(APIView):
    def get(self, request):
        return get_products(request)

    def post(self, request):
        return create_product(request)
