from django.urls import path

from applications.company.api.api import (
    CountryListCreateView,
    CountryRetrieveUpdateDestroyView,
    RegionListCreateView,
    RegionRetrieveUpdateDestroyView,
    CommuneListCreateView,
    CommuneRetrieveUpdateDestroyView,
    MutualSecurityListCreateView,
    MutualSecurityRetrieveUpdateDestroyView,
    BoxesCompensationListCreateView,
    BoxesCompensationRetrieveUpdateDestroyView,
    CompanyListCreateView,
    CompanyRetrieveUpdateDestroyView,
    SubsidiaryListCreateView,
    SubsidiaryRetrieveUpdateDestroyView,
    AreaListCreateView,
    AreaRetrieveUpdateDestroyView,
    DepartmentListCreateView,
    DepartmentRetrieveUpdateDestroyView,
    PositionListCreateView,
    PositionRetrieveUpdateDestroyView,
    CenterCostListCreateView,
    CenterCostRetrieveUpdateDestroyView,
    HealthListCreateView,
    HealthRetrieveUpdateDestroyView,
    AfpListCreateView,
    AfpRetrieveUpdateDestroyView,
    InstitutionsApvListCreateView,
    InstitutionsApvRetrieveUpdateDestroyView,
    BankListCreateView,
    BankRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyView.as_view(), name='country-detail'),

    path('regions/', RegionListCreateView.as_view(), name='region-list-create'),
    path('regions/<int:pk>/', RegionRetrieveUpdateDestroyView.as_view(), name='region-detail'), 

    path('communes/', CommuneListCreateView.as_view(), name='commune-list-create'),
    path('communes/<int:pk>/', CommuneRetrieveUpdateDestroyView.as_view(), name='commune-detail'),

    path('mutual-securities/', MutualSecurityListCreateView.as_view(), name='mutual-security-list-create'),
    path('mutual-securities/<int:pk>/', MutualSecurityRetrieveUpdateDestroyView.as_view(), name='mutual-security-detail'),

    path('boxes-compensations/', BoxesCompensationListCreateView.as_view(), name='boxes-compensation-list-create'),
    path('boxes-compensations/<int:pk>/', BoxesCompensationRetrieveUpdateDestroyView.as_view(), name='boxes-compensation-detail'),

    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),

    path('subsidiaries/', SubsidiaryListCreateView.as_view(), name='subsidiary-list-create'),
    path('subsidiaries/<int:pk>/', SubsidiaryRetrieveUpdateDestroyView.as_view(), name='subsidiary-detail'),

    path('areas/', AreaListCreateView.as_view(), name='area-list-create'),
    path('areas/<int:pk>/', AreaRetrieveUpdateDestroyView.as_view(), name='area-detail'),

    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyView.as_view(), name='department-detail'),

    path('positions/', PositionListCreateView.as_view(), name='position-list-create'),
    path('positions/<int:pk>/', PositionRetrieveUpdateDestroyView.as_view(), name='position-detail'),

    path('center-costs/', CenterCostListCreateView.as_view(), name='center-cost-list-create'),
    path('center-costs/<int:pk>/', CenterCostRetrieveUpdateDestroyView.as_view(), name='center-cost-detail'),

    path('healths/', HealthListCreateView.as_view(), name='health-list-create'),
    path('healths/<int:pk>/', HealthRetrieveUpdateDestroyView.as_view(), name='health-detail'),

    path('afps/', AfpListCreateView.as_view(), name='afp-list-create'),
    path('afps/<int:pk>/', AfpRetrieveUpdateDestroyView.as_view(), name='afp-detail'),

    path('institutions-apvs/', InstitutionsApvListCreateView.as_view(), name='institutions-apv-list-create'),
    path('institutions-apvs/<int:pk>/', InstitutionsApvRetrieveUpdateDestroyView.as_view(), name='institutions-apv-detail'),

    path('banks/', BankListCreateView.as_view(), name='bank-list-create'),
    path('banks/<int:pk>/', BankRetrieveUpdateDestroyView.as_view(), name='bank-detail'),
]
