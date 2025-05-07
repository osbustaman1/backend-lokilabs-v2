from django.urls import path

from applications.security.api.api import (
    ListItemsListCreateView,
    ListItemsRetrieveUpdateDestroyView,
    ListSubItemsDetailView,
    ListSubItemsListCreateView,
    MenuItemsDetailView,
    MenuItemsListCreateView,
    MenuListCreateView, 
    MenuRetrieveUpdateDestroyView
)

urlpatterns = [
    path('menus/', MenuListCreateView.as_view(), name='menu-list-create'),
    path('menus/<int:pk>/', MenuRetrieveUpdateDestroyView.as_view(), name='menu-detail'),  

    path('list-items/', ListItemsListCreateView.as_view(), name='listitems-list-create'),
    path('list-items/<int:pk>/', ListItemsRetrieveUpdateDestroyView.as_view(), name='listitems-detail'),

    path('list-sub-items/', ListSubItemsListCreateView.as_view(), name='subitems-list'),
    path('list-sub-items/<int:pk>/', ListSubItemsDetailView.as_view(), name='subitems-detail'),

    path('menu-items/', MenuItemsListCreateView.as_view(), name='menuitems-list'),
    path('menu-items/<int:pk>/', MenuItemsDetailView.as_view(), name='menuitems-detail'),
]
