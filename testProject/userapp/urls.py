

from django.urls import path
from .views import RegisterView
from .views import RegisterAdminView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('admin/', RegisterAdminView.as_view(), name='register-admin'),
]