from rest_framework.views import APIView

from ..service.category_service import get_categories
from ..service.category_service import create_category

class CategoryView(APIView):
    def get(self, request):
        return get_categories(request)

    def post(self, request):
        return create_category(request)
