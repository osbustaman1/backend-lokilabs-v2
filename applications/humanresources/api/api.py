from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from remunerations.decorators import verify_token_cls

@verify_token_cls
class ProtectedApiView(generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        return Response({'message': 'Protected API endpoint'}, status=status.HTTP_200_OK)