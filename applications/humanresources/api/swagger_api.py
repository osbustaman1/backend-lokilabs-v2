from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


jwt_header = openapi.Parameter(
    'token',
    openapi.IN_HEADER,
    description="Token de autenticación JWT",
    type=openapi.TYPE_STRING,
    required=True
)


create_user = swagger_auto_schema(
    operation_description="Crear usuario.",
    manual_parameters=[jwt_header],
    request_body=UserSerializer,
    responses={
        200: UserSerializer(many=True),
        201: UserSerializer,
        401: openapi.Response("Unauthorized"),
    }
)
