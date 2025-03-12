

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .settings import SWAGGER_PERMISSION
from userapp import permissions
permission = [permissions.IsAdmin]


if SWAGGER_PERMISSION == "ALL":
    from rest_framework import permissions
    permission = [permissions.AllowAny]


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="Документация для API",
    ),
    public=True,
    permission_classes=permission,
)