from rest_framework.views import APIView

from ..service.products_service import getProducts

class ProductsView(APIView):

    def post(self, request):
        return getProducts(request)
