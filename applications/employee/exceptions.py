from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if isinstance(exc, (InvalidToken, TokenError)):
        return Response(
            {'detail': 'Sesión expirada. Por favor inicie sesión nuevamente.', 'code': 'token_expired'},
            status=401
        )
    
    return response