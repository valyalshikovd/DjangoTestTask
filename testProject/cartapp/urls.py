from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CartView


router = DefaultRouter()
router.register('', CartView, basename='carts')
urlpatterns = router.urls
