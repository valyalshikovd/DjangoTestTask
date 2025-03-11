from rest_framework.decorators import permission_classes, action
from rest_framework.views import APIView

from ..service.category_service import get_categories
from ..service.category_service import create_category
from userapp import permissions


class CategoryView(APIView):
    def get(self, request):
        return get_categories(request)

    @action(detail=False, permission_classes=[permissions.permissions.IsAdminUser])
    def post(self, request):
        return create_category(request)
