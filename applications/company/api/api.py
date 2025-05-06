from applications.company.api.swagger_api import *
from applications.company.api.serializer import (
    CountrySerializer, 
    RegionSerializer, 
    CommuneSerializer, 
    MutualSecuritySerializer, 
    BoxesCompensationSerializer,
    CompanySerializer,
    SubsidiarySerializer,
    AreaSerializer,
    DepartmentSerializer,
    PositionSerializer,
    CenterCostSerializer,
    HealthSerializer,
    AfpSerializer,
    InstitutionsApvSerializer,
    BankSerializer
)
from applications.company.models import (
    MutualSecurity, 
    BoxesCompensation,
    Company, 
    Subsidiary, 
    Area, 
    Department, 
    Position, 
    CenterCost,
    Health,
    Afp,
    InstitutionsApv,
    Bank
)
from applications.security.models import Country, Region, Commune
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from remunerations.decorators import verify_token_cls
from rest_framework import generics, status
from rest_framework.response import Response

@method_decorator(country_list_schema, name='get')
@method_decorator(country_create_schema, name='post')
@verify_token_cls
class CountryListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de países.

    - GET: Obtiene la lista de países.
    - POST: Crea un nuevo país.

    Decoradores:
    - `country_list_schema`: Documenta el GET.
    - `country_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todos los países.
    - serializer_class: CountrySerializer.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


@method_decorator(country_detail_schema, name='get')
@method_decorator(country_update_schema, name='put')
@method_decorator(country_delete_schema, name='delete')
@verify_token_cls
class CountryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar un país por ID.

    Métodos documentados:
    - `country_detail_schema`: GET
    - `country_update_schema`: PUT
    - `country_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todos los países.
    - serializer_class: CountrySerializer.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


@method_decorator(region_list_schema, name='get')
@method_decorator(region_create_schema, name='post')
@verify_token_cls
class RegionListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de regiones.

    - GET: Obtiene la lista de regiones.
    - POST: Crea una nueva región.

    Decoradores:
    - `region_list_schema`: Documenta el GET.
    - `region_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todas las regiones.
    - serializer_class: RegionSerializer.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

@method_decorator(region_detail_schema, name='get')
@method_decorator(region_update_schema, name='put')
@method_decorator(region_delete_schema, name='delete')
@verify_token_cls
class RegionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar una región por ID.

    Métodos documentados:
    - `region_detail_schema`: GET
    - `region_update_schema`: PUT
    - `region_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todas las regiones.
    - serializer_class: RegionSerializer.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


@method_decorator(commune_list_schema, name='get')
@method_decorator(commune_create_schema, name='post')
@verify_token_cls
class CommuneListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de comunas.

    - GET: Obtiene la lista de comunas.
    - POST: Crea una nueva comuna.

    Decoradores:
    - `commune_list_schema`: Documenta el GET.
    - `commune_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todas las comunas.
    - serializer_class: CommuneSerializer.
    """
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer

@method_decorator(commune_detail_schema, name='get')
@method_decorator(commune_update_schema, name='put')
@method_decorator(commune_delete_schema, name='delete')
@verify_token_cls
class CommuneRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar una comuna por ID.

    Métodos documentados:
    - `commune_detail_schema`: GET
    - `commune_update_schema`: PUT
    - `commune_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todas las comunas.
    - serializer_class: CommuneSerializer.
    """
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer



@method_decorator(mutual_security_list_schema, name='get')
@method_decorator(mutual_security_create_schema, name='post')
@verify_token_cls
class MutualSecurityListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de mutuales de seguridad.

    - GET: Obtiene la lista de mutuales.
    - POST: Crea una nueva mutual.

    Decoradores:
    - `mutual_security_list_schema`: Documenta el GET.
    - `mutual_security_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todas las mutuales de seguridad.
    - serializer_class: MutualSecuritySerializer.
    """
    queryset = MutualSecurity.objects.all()
    serializer_class = MutualSecuritySerializer

@method_decorator(mutual_security_detail_schema, name='get')
@method_decorator(mutual_security_update_schema, name='put')
@method_decorator(mutual_security_delete_schema, name='delete')
@verify_token_cls
class MutualSecurityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar una mutual de seguridad por ID.

    Métodos documentados:
    - `mutual_security_detail_schema`: GET
    - `mutual_security_update_schema`: PUT
    - `mutual_security_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todas las mutuales de seguridad.
    - serializer_class: MutualSecuritySerializer.
    """
    queryset = MutualSecurity.objects.all()
    serializer_class = MutualSecuritySerializer


@method_decorator(boxes_compensation_list_schema, name='get')
@method_decorator(boxes_compensation_create_schema, name='post')
@verify_token_cls
class BoxesCompensationListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de cajas de compensación.

    - GET: Obtiene la lista de cajas de compensación.
    - POST: Crea una nueva caja de compensación.

    Decoradores:
    - `boxes_compensation_list_schema`: Documenta el GET.
    - `boxes_compensation_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todas las cajas de compensación.
    - serializer_class: BoxesCompensationSerializer.
    """
    queryset = BoxesCompensation.objects.all()
    serializer_class = BoxesCompensationSerializer

@method_decorator(boxes_compensation_detail_schema, name='get')
@method_decorator(boxes_compensation_update_schema, name='put')
@method_decorator(boxes_compensation_delete_schema, name='delete')
@verify_token_cls
class BoxesCompensationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar una caja de compensación por ID.

    Métodos documentados:
    - `boxes_compensation_detail_schema`: GET
    - `boxes_compensation_update_schema`: PUT
    - `boxes_compensation_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todas las cajas de compensación.
    - serializer_class: BoxesCompensationSerializer.
    """
    queryset = BoxesCompensation.objects.all()
    serializer_class = BoxesCompensationSerializer


@method_decorator(company_list_schema, name='get')
@method_decorator(company_create_schema, name='post')
@verify_token_cls
class CompanyListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de empresas.

    - GET: Obtiene la lista de empresas.
    - POST: Crea una nueva empresa.

    Decoradores:
    - `company_list_schema`: Documenta el GET.
    - `company_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todas las empresas.
    - serializer_class: CompanySerializer.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

@method_decorator(company_detail_schema, name='get')
@method_decorator(company_update_schema, name='put')
@method_decorator(company_delete_schema, name='delete')
@verify_token_cls
class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar una empresa por ID.

    Métodos documentados:
    - `company_detail_schema`: GET
    - `company_update_schema`: PUT
    - `company_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todas las empresas.
    - serializer_class: CompanySerializer.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


@method_decorator(subsidiary_list_schema, name='get')
@method_decorator(subsidiary_create_schema, name='post')
@verify_token_cls
class SubsidiaryListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de sucursales.

    - GET: Obtiene la lista de sucursales.
    - POST: Crea una nueva sucursal.

    Decoradores:
    - `subsidiary_list_schema`: Documenta el GET.
    - `subsidiary_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todas las sucursales.
    - serializer_class: SubsidiarySerializer.
    """
    queryset = Subsidiary.objects.all()
    serializer_class = SubsidiarySerializer

@method_decorator(subsidiary_detail_schema, name='get')
@method_decorator(subsidiary_update_schema, name='put')
@method_decorator(subsidiary_delete_schema, name='delete')
@verify_token_cls
class SubsidiaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar una sucursal por ID.

    Métodos documentados:
    - `subsidiary_detail_schema`: GET
    - `subsidiary_update_schema`: PUT
    - `subsidiary_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todas las sucursales.
    - serializer_class: SubsidiarySerializer.
    """
    queryset = Subsidiary.objects.all()
    serializer_class = SubsidiarySerializer


@method_decorator(area_list_schema, name='get')
@method_decorator(area_create_schema, name='post')
@verify_token_cls
class AreaListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de áreas.

    - GET: Obtiene la lista de áreas.
    - POST: Crea una nueva área.

    Decoradores:
    - `area_list_schema`: Documenta el GET.
    - `area_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todas las áreas.
    - serializer_class: AreaSerializer.
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

@method_decorator(area_detail_schema, name='get')
@method_decorator(area_update_schema, name='put')
@method_decorator(area_delete_schema, name='delete')
@verify_token_cls
class AreaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar un área por ID.

    Métodos documentados:
    - `area_detail_schema`: GET
    - `area_update_schema`: PUT
    - `area_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todas las áreas.
    - serializer_class: AreaSerializer.
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


@method_decorator(department_list_schema, name='get')
@method_decorator(department_create_schema, name='post')
@verify_token_cls
class DepartmentListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de departamentos.

    - GET: Obtiene la lista de departamentos.
    - POST: Crea un nuevo departamento.

    Decoradores:
    - `department_list_schema`: Documenta el GET.
    - `department_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todos los departamentos.
    - serializer_class: DepartmentSerializer.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

@method_decorator(department_detail_schema, name='get')
@method_decorator(department_update_schema, name='put')
@method_decorator(department_delete_schema, name='delete')
@verify_token_cls
class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar un departamento por ID.

    Métodos documentados:
    - `department_detail_schema`: GET
    - `department_update_schema`: PUT
    - `department_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todos los departamentos.
    - serializer_class: DepartmentSerializer.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


@method_decorator(position_list_schema, name='get')
@method_decorator(position_create_schema, name='post')
@verify_token_cls
class PositionListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de cargos.

    - GET: Obtiene la lista de cargos.
    - POST: Crea un nuevo cargo.

    Decoradores:
    - `position_list_schema`: Documenta el GET.
    - `position_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todos los cargos.
    - serializer_class: PositionSerializer.
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

@method_decorator(position_detail_schema, name='get')
@method_decorator(position_update_schema, name='put')
@method_decorator(position_delete_schema, name='delete')
@verify_token_cls
class PositionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar un cargo por ID.

    Métodos documentados:
    - `position_detail_schema`: GET
    - `position_update_schema`: PUT
    - `position_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todos los cargos.
    - serializer_class: PositionSerializer.
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


@method_decorator(center_cost_list_schema, name='get')
@method_decorator(center_cost_create_schema, name='post')
@verify_token_cls
class CenterCostListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de centros de costo.

    - GET: Obtiene la lista de centros de costo.
    - POST: Crea un nuevo centro de costo.

    Decoradores:
    - `center_cost_list_schema`: Documenta el GET.
    - `center_cost_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todos los centros de costo.
    - serializer_class: CenterCostSerializer.
    """
    queryset = CenterCost.objects.all()
    serializer_class = CenterCostSerializer

@method_decorator(center_cost_detail_schema, name='get')
@method_decorator(center_cost_update_schema, name='put')
@method_decorator(center_cost_delete_schema, name='delete')
@verify_token_cls
class CenterCostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar un centro de costo por ID.

    Métodos documentados:
    - `center_cost_detail_schema`: GET
    - `center_cost_update_schema`: PUT
    - `center_cost_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todos los centros de costo.
    - serializer_class: CenterCostSerializer.
    """
    queryset = CenterCost.objects.all()
    serializer_class = CenterCostSerializer


@method_decorator(health_list_schema, name='get')
@method_decorator(health_create_schema, name='post')
@verify_token_cls
class HealthListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de entidades de salud.

    - GET: Obtiene la lista de entidades de salud.
    - POST: Crea una nueva entidad de salud.

    Decoradores:
    - `health_list_schema`: Documenta el GET.
    - `health_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todas las entidades de salud.
    - serializer_class: HealthSerializer.
    """
    queryset = Health.objects.all()
    serializer_class = HealthSerializer

@method_decorator(health_detail_schema, name='get')
@method_decorator(health_update_schema, name='put')
@method_decorator(health_delete_schema, name='delete')
@verify_token_cls
class HealthRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar una entidad de salud por ID.

    Métodos documentados:
    - `health_detail_schema`: GET
    - `health_update_schema`: PUT
    - `health_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todas las entidades de salud.
    - serializer_class: HealthSerializer.
    """
    queryset = Health.objects.all()
    serializer_class = HealthSerializer


@method_decorator(afp_list_schema, name='get')
@method_decorator(afp_create_schema, name='post')
@verify_token_cls
class AfpListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de AFP.

    - GET: Obtiene la lista de AFP.
    - POST: Crea una nueva AFP.

    Decoradores:
    - `afp_list_schema`: Documenta el GET.
    - `afp_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todas las AFP.
    - serializer_class: AfpSerializer.
    """
    queryset = Afp.objects.all()
    serializer_class = AfpSerializer

@method_decorator(afp_detail_schema, name='get')
@method_decorator(afp_update_schema, name='put')
@method_decorator(afp_delete_schema, name='delete')
@verify_token_cls
class AfpRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar una AFP por ID.

    Métodos documentados:
    - `afp_detail_schema`: GET
    - `afp_update_schema`: PUT
    - `afp_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todas las AFP.
    - serializer_class: AfpSerializer.
    """
    queryset = Afp.objects.all()
    serializer_class = AfpSerializer


@method_decorator(institutions_apv_list_schema, name='get')
@method_decorator(institutions_apv_create_schema, name='post')
@verify_token_cls
class InstitutionsApvListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de instituciones APV.

    - GET: Obtiene la lista de instituciones APV.
    - POST: Crea una nueva institución APV.

    Decoradores:
    - `institutions_apv_list_schema`: Documenta el GET.
    - `institutions_apv_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todas las instituciones APV.
    - serializer_class: InstitutionsApvSerializer.
    """
    queryset = InstitutionsApv.objects.all()
    serializer_class = InstitutionsApvSerializer

@method_decorator(institutions_apv_detail_schema, name='get')
@method_decorator(institutions_apv_update_schema, name='put')
@method_decorator(institutions_apv_delete_schema, name='delete')
@verify_token_cls
class InstitutionsApvRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar una institución APV por ID.

    Métodos documentados:
    - `institutions_apv_detail_schema`: GET
    - `institutions_apv_update_schema`: PUT
    - `institutions_apv_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todas las instituciones APV.
    - serializer_class: InstitutionsApvSerializer.
    """
    queryset = InstitutionsApv.objects.all()
    serializer_class = InstitutionsApvSerializer



@method_decorator(bank_list_schema, name='get')
@method_decorator(bank_create_schema, name='post')
@verify_token_cls
class BankListCreateView(generics.ListCreateAPIView):
    """
    View para manejar la obtención y creación de bancos.

    - GET: Obtiene la lista de bancos.
    - POST: Crea un nuevo banco.

    Decoradores:
    - `bank_list_schema`: Documenta el GET.
    - `bank_create_schema`: Documenta el POST.
    - `verify_token_cls`: Requiere autenticación por JWT.

    Atributos:
    - queryset: Todos los bancos.
    - serializer_class: BankSerializer.
    """
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

@method_decorator(bank_detail_schema, name='get')
@method_decorator(bank_update_schema, name='put')
@method_decorator(bank_delete_schema, name='delete')
@verify_token_cls
class BankRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para obtener, actualizar o eliminar un banco por ID.

    Métodos documentados:
    - `bank_detail_schema`: GET
    - `bank_update_schema`: PUT
    - `bank_delete_schema`: DELETE

    También requiere autenticación con `verify_token_cls`.

    Atributos:
    - queryset: Todos los bancos.
    - serializer_class: BankSerializer.
    """
    queryset = Bank.objects.all()
    serializer_class = BankSerializer