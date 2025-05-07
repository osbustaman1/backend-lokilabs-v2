from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from remunerations.decorators import verify_token_cls
from rest_framework import generics, status
from rest_framework.response import Response

from applications.employee.api.serializer import EmployeeSerializer, UserCompanySerializer, UserTypeContractSerializer
from applications.employee.api.swagger_api import (
    employee_list_schema,
    employee_create_schema,
    employee_detail_schema,
    employee_update_schema,
    employee_delete_schema,

    user_company_list_schema,
    user_company_create_schema,
    user_company_detail_schema,
    user_company_update_schema,
    user_company_delete_schema,

    user_type_contract_list_schema,
    user_type_contract_create_schema,
    user_type_contract_detail_schema,
    user_type_contract_update_schema,
    user_type_contract_delete_schema,

)
from applications.employee.models import Employee, UserCompany, UserTypeContract


@method_decorator(employee_list_schema, name='get')
@method_decorator(employee_create_schema, name='post')
@verify_token_cls
class EmployeeListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de empleados

    - GET: Lista de empleados
    - POST: Crea nuevo empleado

    Decoradores:
    - JWT requerido mediante verify_token_cls
    - Esquemas Swagger para documentación
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

@method_decorator(employee_detail_schema, name='get')
@method_decorator(employee_update_schema, name='put')
@method_decorator(employee_delete_schema, name='delete')
@verify_token_cls
class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para operaciones CRUD detalladas de empleados

    Métodos soportados:
    - GET: Obtiene detalle
    - PUT: Actualización completa
    - DELETE: Eliminación

    Requiere autenticación JWT
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@method_decorator(user_company_list_schema, name='get')
@method_decorator(user_company_create_schema, name='post')
@verify_token_cls
class UserCompanyListCreateView(generics.ListCreateAPIView):
    """
    View para gestionar relaciones usuario-empresa

    - GET: Lista todas las relaciones
    - POST: Crea nueva relación
    """
    queryset = UserCompany.objects.all()
    serializer_class = UserCompanySerializer


@method_decorator(user_company_detail_schema, name='get')
@method_decorator(user_company_update_schema, name='put')
@method_decorator(user_company_delete_schema, name='delete')
@verify_token_cls
class UserCompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para operaciones detalladas en relaciones usuario-empresa

    - GET: Detalle de relación
    - PUT: Actualización completa
    - DELETE: Eliminación
    """
    queryset = UserCompany.objects.all()
    serializer_class = UserCompanySerializer


@method_decorator(user_type_contract_list_schema, name='get')
@method_decorator(user_type_contract_create_schema, name='post')
@verify_token_cls
class UserTypeContractListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de contratos de usuario.

    - GET: Obtiene la lista de contratos.
    - POST: Crea un nuevo contrato.

    Decoradores:
    - `user_type_contract_list_schema`: Documenta el GET.
    - `user_type_contract_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todos los contratos de usuario.
    - serializer_class: UserTypeContractSerializer.
    """
    queryset = UserTypeContract.objects.all()
    serializer_class = UserTypeContractSerializer


@method_decorator(user_type_contract_detail_schema, name='get')
@method_decorator(user_type_contract_update_schema, name='put')
@method_decorator(user_type_contract_delete_schema, name='delete')
@verify_token_cls
class UserTypeContractRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar un contrato por ID.

    Métodos documentados:
    - `user_type_contract_detail_schema`: GET
    - `user_type_contract_update_schema`: PUT
    - `user_type_contract_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todos los contratos de usuario.
    - serializer_class: UserTypeContractSerializer.
    """
    queryset = UserTypeContract.objects.all()
    serializer_class = UserTypeContractSerializer


@method_decorator(user_company_list_schema, name='get')
@method_decorator(user_company_create_schema, name='post')
@verify_token_cls
class ListUserCompanyCreateView(generics.ListCreateAPIView):
    """
    View para gestionar relaciones usuario-empresa.

    - GET: Lista todas las relaciones de usuarios de una empresa específica.
    - POST: Crea nueva relación usuario-empresa.

    Filtro:
    - Se filtra por el parámetro `id_emp` (ID de la empresa).
    """
    serializer_class = UserCompanySerializer

    def get_queryset(self):
        """
        Filtra las relaciones usuario-empresa por el ID de la empresa.
        """
        id_emp = self.kwargs.get('id_emp')  # Obtiene el parámetro de la URL
        return UserCompany.objects.filter(company__com_id=id_emp)