from django.urls import path
from applications.humanresources.api.api import ProtectedApiView

urlpatterns = [
    path('list-banks', ProtectedApiView.as_view(), name='ListBanksView'),
]