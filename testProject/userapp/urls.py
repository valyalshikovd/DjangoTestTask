

from django.urls import path
from .views import RegisterView, MailConfirmation
from .views import RegisterAdminView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('admin/', RegisterAdminView.as_view(), name='register-admin'),
    path('mail_confirm/', MailConfirmation.as_view(), name='mail-confirm'),
]