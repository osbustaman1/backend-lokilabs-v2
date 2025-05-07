from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from applications.security.api.serializer import (
    ListItemsSerializer, 
    ListSubItemsSerializer, 
    MenuItemsSerializer, 
    MenuSerializer
)
from applications.security.models import (
    ListItems, 
    ListSubItems, 
    Menu, 
    MenuItems
)
from remunerations.decorators import verify_token_cls
from rest_framework import generics, status
from rest_framework.response import Response

from applications.security.api.swagger_api import (
    menu_list_schema,
    menu_create_schema,
    menu_detail_schema,
    menu_update_schema,
    menu_delete_schema,

    listitems_list_schema,
    listitems_create_schema,
    listitems_detail_schema,
    listitems_update_schema,
    listitems_delete_schema,

    listsubitems_list_schema,
    listsubitems_create_schema,
    listsubitems_detail_schema,
    listsubitems_update_schema,
    listsubitems_delete_schema,

    menuitems_list_schema,
    menuitems_create_schema,
    menuitems_detail_schema,
    menuitems_update_schema,
    menuitems_delete_schema
)


@method_decorator(menu_list_schema, name='get')
@method_decorator(menu_create_schema, name='post')
@verify_token_cls
class MenuListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de menús

    - GET: Lista todos los menús
    - POST: Crea nuevo menú

    Decoradores:
    - JWT requerido mediante verify_token_cls
    - Esquemas Swagger para documentación
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

@method_decorator(menu_detail_schema, name='get')
@method_decorator(menu_update_schema, name='put')
@method_decorator(menu_delete_schema, name='delete')
@verify_token_cls
class MenuRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para operaciones CRUD detalladas de menús

    Métodos soportados:
    - GET: Obtiene detalle
    - PUT: Actualización completa
    - DELETE: Eliminación

    Requiere autenticación JWT
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


@method_decorator(listitems_list_schema, name='get')
@method_decorator(listitems_create_schema, name='post')
@verify_token_cls
class ListItemsListCreateView(generics.ListCreateAPIView):
    """
    View para gestión de ítems de menú
    
    - GET: Lista todos los ítems
    - POST: Crea nuevo ítem
    Requiere autenticación JWT
    """
    queryset = ListItems.objects.all()
    serializer_class = ListItemsSerializer

@method_decorator(listitems_detail_schema, name='get')
@method_decorator(listitems_update_schema, name='put')
@method_decorator(listitems_delete_schema, name='delete')
@verify_token_cls
class ListItemsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para operaciones detalladas de ítems
    
    - GET: Detalle del ítem
    - PUT: Actualización completa
    - DELETE: Eliminación
    Requiere autenticación JWT
    """
    queryset = ListItems.objects.all()
    serializer_class = ListItemsSerializer


@method_decorator(listsubitems_list_schema, name='get')
@method_decorator(listsubitems_create_schema, name='post')
@verify_token_cls
class ListSubItemsListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar y crear subitems de menú
    - GET: Lista jerarquía completa de menús
    - POST: Crea nuevo subitem con relación a item padre
    """
    queryset = ListSubItems.objects.all()
    serializer_class = ListSubItemsSerializer

@method_decorator(listsubitems_detail_schema, name='get')
@method_decorator(listsubitems_update_schema, name='put')
@method_decorator(listsubitems_delete_schema, name='delete')
@verify_token_cls
class ListSubItemsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para operaciones específicas en subitems
    - GET: Detalle completo con relaciones
    - PUT: Actualización total del registro
    - DELETE: Eliminación lógica (cambia estado active)
    """
    queryset = ListSubItems.objects.all()
    serializer_class = ListSubItemsSerializer


@method_decorator(menuitems_list_schema, name='get')
@method_decorator(menuitems_create_schema, name='post')
@verify_token_cls
class MenuItemsListCreateView(generics.ListCreateAPIView):
    """
    Vista para gestionar relaciones entre menús e ítems
    - GET: Lista todas las relaciones existentes
    - POST: Asocia un ítem a un menú
    """
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

@method_decorator(menuitems_detail_schema, name='get')
@method_decorator(menuitems_update_schema, name='put')
@method_decorator(menuitems_delete_schema, name='delete')
@verify_token_cls
class MenuItemsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para operaciones específicas en relaciones
    - GET: Muestra detalle de la relación
    - PUT: Actualiza ambos campos de la relación
    - DELETE: Elimina la asociación
    """
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer