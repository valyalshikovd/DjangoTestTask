from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from .service import add_user
from .service import mail_confirmation
from .serializers import RegisterSerializer

@swagger_auto_schema(
    operation_description="Добавить товар в коррзину",
    request_body=RegisterSerializer,
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
class RegisterView(APIView):
    def post(self, request):
        return add_user(request=request, permission="AuthorizeUser")



class RegisterAdminView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        return add_user(request=request, permission="Admining")

class MailConfirmation(APIView):

    @swagger_auto_schema(
        operation_description="Подтвердить потчу",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description="Почта"),
                'code': openapi.Schema(type=openapi.TYPE_STRING, description="Код из почты"),
            },
        ),
        responses={200: openapi.Response("Успешный ответ")}
    )
    def post(self, request):
        return mail_confirmation(request)
