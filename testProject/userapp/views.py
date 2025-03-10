from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from .service import add_user

class RegisterView(APIView):
    def post(self, request):
        return add_user(request=request, permission="AuthorizeUser")


class RegisterAdminView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        return add_user(request=request, permission="Admining")
