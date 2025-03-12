from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from userapp import permissions
from .service import create
# Create your views here.
class OrderView(ViewSet):
    permission_classes = [permissions.IsAuthorizeUser]

    def create(self, request):
        return create(request)
