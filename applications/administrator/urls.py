from django.urls import path

from applications.administrator.api.api import (
    CommuneListCreateView,
    CountryListCreateView,
    RegionListCreateView,

    CreateUserView,
    ListAdminUsersView,
    ListCustomersView,
    CreateCustomerView,
    GetCustomerDataView,
    
    UpdateCustomerView
)

app_name = 'administrator_app'

urlpatterns = [

    path('create-user/<int:pk>/', CreateUserView.as_view(), name='create_user'),
    path('list-admin-users/<int:pk>/', ListAdminUsersView.as_view(), name='list_admin_users'),

    path('listado-clientes', ListCustomersView.as_view(), name='ListCustomersView'),
    path('add-customers', CreateCustomerView.as_view(), name='CreateCustomerView'),
    path('get-data-customer', CreateCustomerView.as_view(), name='CreateCustomerView'),

    path('get-data-customer/<int:pk>/', GetCustomerDataView.as_view(), name='CreateCustomerView'),
    path('update-data-customer/<int:pk>/', UpdateCustomerView.as_view(), name='UpdateCustomerView'),












    path('list-countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('list-region/', RegionListCreateView.as_view(), name='region-list-create'),
    path('list-commune/', CommuneListCreateView.as_view(), name='commune-list-create'),

]
