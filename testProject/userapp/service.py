from rest_framework import status

from .serializers import RegisterSerializer
from rest_framework.response import Response

def add_user(request, permission):
    data = request.data | {"permission": permission}
    print(data)
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Пользователь зарегистрирован"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)