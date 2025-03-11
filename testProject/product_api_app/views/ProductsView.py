from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from ..service.products_service import getProducts

class ProductsView(ViewSet):

    @action(detail=False, methods=['post'])
    def getProducts(self, request):
        return getProducts(request)
