from django.urls import path

from applications.employee.api.api import (
    EmployeeListCreateView, 
    EmployeeRetrieveUpdateDestroyView,
    UserCompanyListCreateView,
    UserCompanyRetrieveUpdateDestroyView,
    UserTypeContractListCreateView,
    UserTypeContractRetrieveUpdateDestroyView,
    ListUserCompanyCreateView
)



urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),

    path('user-companies/', UserCompanyListCreateView.as_view(), name='user-company-list-create'),
    path('user-companies/<int:pk>/', UserCompanyRetrieveUpdateDestroyView.as_view(), name='user-company-detail'),

    path('user-type-contracts/', UserTypeContractListCreateView.as_view(), name='user-type-contract-list-create'),
    path('user-type-contracts/<int:pk>/', UserTypeContractRetrieveUpdateDestroyView.as_view(), name='user-type-contract-detail'),

    path('list-user-company/<int:id_emp>/', ListUserCompanyCreateView.as_view(), name='list-user-company'),
]
