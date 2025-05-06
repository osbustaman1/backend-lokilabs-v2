from django.urls import path
from applications.humanresources.api.api import ProtectedApiView

urlpatterns = [
    path('api/test/', ProtectedApiView.as_view(), name='ProtectedApiView'),
]