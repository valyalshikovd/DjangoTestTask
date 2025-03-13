from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.response import Response
from .redis_service import get_cache
from .smtp_client_service import send_verification_email


def add_user(request, permission):
    data = request.data | {"permission": permission}
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        send_verification_email.delay(data['email'])
        return Response({"message": "Пользователь зарегистрирован"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def mail_confirmation(request):

    email = request.data['email']
    code = get_cache(email)
    data = request.data['code']
    user = get_object_or_404(User, email=email)

    if code == data:
        user.is_active = True
        user.save()
        return Response("success", status=status.HTTP_200_OK)
    return Response("неправильный код", status=status.HTTP_400_BAD_REQUEST)