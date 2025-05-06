from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

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

jwt_header = openapi.Parameter(
    'token',
    openapi.IN_HEADER,
    description="Token de autenticación JWT",
    type=openapi.TYPE_STRING,
    required=True
)


# Documentación para obtener la lista de países (GET)
country_list_schema = swagger_auto_schema(
    operation_description="Lista todos los países registrados. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: CountrySerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear un nuevo país (POST)
country_create_schema = swagger_auto_schema(
    operation_description="Crea un nuevo país. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=CountrySerializer,
    responses={
        201: CountrySerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener un país por ID (GET)
country_detail_schema = swagger_auto_schema(
    operation_description="Obtiene un país específico por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: CountrySerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("País no encontrado"),
    }
)

# Documentación para actualizar un país (PUT)
country_update_schema = swagger_auto_schema(
    operation_description="Actualiza un país por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=CountrySerializer,
    responses={
        200: CountrySerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("País no encontrado"),
    }
)

# Documentación para eliminar un país (DELETE)
country_delete_schema = swagger_auto_schema(
    operation_description="Elimina un país por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("País eliminado con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("País no encontrado"),
    }
)


# Documentación para obtener la lista de regiones (GET)
region_list_schema = swagger_auto_schema(
    operation_description="Lista todas las regiones registradas. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: RegionSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear una nueva región (POST)
region_create_schema = swagger_auto_schema(
    operation_description="Crea una nueva región. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=RegionSerializer,
    responses={
        201: RegionSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener una región por ID (GET)
region_detail_schema = swagger_auto_schema(
    operation_description="Obtiene una región específica por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: RegionSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Región no encontrada"),
    }
)

# Documentación para actualizar una región (PUT)
region_update_schema = swagger_auto_schema(
    operation_description="Actualiza una región por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=RegionSerializer,
    responses={
        200: RegionSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Región no encontrada"),
    }
)

# Documentación para eliminar una región (DELETE)
region_delete_schema = swagger_auto_schema(
    operation_description="Elimina una región por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Región eliminada con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Región no encontrada"),
    }
)

# Documentación para obtener la lista de comunas (GET)
commune_list_schema = swagger_auto_schema(
    operation_description="Lista todas las comunas registradas. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: CommuneSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear una nueva comuna (POST)
commune_create_schema = swagger_auto_schema(
    operation_description="Crea una nueva comuna. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=CommuneSerializer,
    responses={
        201: CommuneSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener una comuna por ID (GET)
commune_detail_schema = swagger_auto_schema(
    operation_description="Obtiene una comuna específica por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: CommuneSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Comuna no encontrada"),
    }
)

# Documentación para actualizar una comuna (PUT)
commune_update_schema = swagger_auto_schema(
    operation_description="Actualiza una comuna por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=CommuneSerializer,
    responses={
        200: CommuneSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Comuna no encontrada"),
    }
)

# Documentación para eliminar una comuna (DELETE)
commune_delete_schema = swagger_auto_schema(
    operation_description="Elimina una comuna por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Comuna eliminada con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Comuna no encontrada"),
    }
)


# Documentación para obtener la lista de mutuales (GET)
mutual_security_list_schema = swagger_auto_schema(
    operation_description="Lista todas las mutuales de seguridad registradas. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: MutualSecuritySerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear una nueva mutual (POST)
mutual_security_create_schema = swagger_auto_schema(
    operation_description="Crea una nueva mutual de seguridad. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=MutualSecuritySerializer,
    responses={
        201: MutualSecuritySerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener una mutual por ID (GET)
mutual_security_detail_schema = swagger_auto_schema(
    operation_description="Obtiene una mutual de seguridad específica por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: MutualSecuritySerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Mutual no encontrada"),
    }
)

# Documentación para actualizar una mutual (PUT)
mutual_security_update_schema = swagger_auto_schema(
    operation_description="Actualiza una mutual de seguridad por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=MutualSecuritySerializer,
    responses={
        200: MutualSecuritySerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Mutual no encontrada"),
    }
)

# Documentación para eliminar una mutual (DELETE)
mutual_security_delete_schema = swagger_auto_schema(
    operation_description="Elimina una mutual de seguridad por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Mutual eliminada con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Mutual no encontrada"),
    }
)

# Documentación para obtener la lista de cajas de compensación (GET)
boxes_compensation_list_schema = swagger_auto_schema(
    operation_description="Lista todas las cajas de compensación registradas. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: BoxesCompensationSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear una nueva caja de compensación (POST)
boxes_compensation_create_schema = swagger_auto_schema(
    operation_description="Crea una nueva caja de compensación. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=BoxesCompensationSerializer,
    responses={
        201: BoxesCompensationSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener una caja de compensación por ID (GET)
boxes_compensation_detail_schema = swagger_auto_schema(
    operation_description="Obtiene una caja de compensación específica por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: BoxesCompensationSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Caja de compensación no encontrada"),
    }
)

# Documentación para actualizar una caja de compensación (PUT)
boxes_compensation_update_schema = swagger_auto_schema(
    operation_description="Actualiza una caja de compensación por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=BoxesCompensationSerializer,
    responses={
        200: BoxesCompensationSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Caja de compensación no encontrada"),
    }
)

# Documentación para eliminar una caja de compensación (DELETE)
boxes_compensation_delete_schema = swagger_auto_schema(
    operation_description="Elimina una caja de compensación por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Caja de compensación eliminada con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Caja de compensación no encontrada"),
    }
)

# Documentación para obtener la lista de empresas (GET)
company_list_schema = swagger_auto_schema(
    operation_description="Lista todas las empresas registradas. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: CompanySerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear una nueva empresa (POST)
company_create_schema = swagger_auto_schema(
    operation_description="Crea una nueva empresa. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=CompanySerializer,
    responses={
        201: CompanySerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener una empresa por ID (GET)
company_detail_schema = swagger_auto_schema(
    operation_description="Obtiene una empresa específica por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: CompanySerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Empresa no encontrada"),
    }
)

# Documentación para actualizar una empresa (PUT)
company_update_schema = swagger_auto_schema(
    operation_description="Actualiza una empresa por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=CompanySerializer,
    responses={
        200: CompanySerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Empresa no encontrada"),
    }
)

# Documentación para eliminar una empresa (DELETE)
company_delete_schema = swagger_auto_schema(
    operation_description="Elimina una empresa por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Empresa eliminada con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Empresa no encontrada"),
    }
)


# Documentación para obtener la lista de sucursales (GET)
subsidiary_list_schema = swagger_auto_schema(
    operation_description="Lista todas las sucursales registradas. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: SubsidiarySerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear una nueva sucursal (POST)
subsidiary_create_schema = swagger_auto_schema(
    operation_description="Crea una nueva sucursal. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=SubsidiarySerializer,
    responses={
        201: SubsidiarySerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener una sucursal por ID (GET)
subsidiary_detail_schema = swagger_auto_schema(
    operation_description="Obtiene una sucursal específica por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: SubsidiarySerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Sucursal no encontrada"),
    }
)

# Documentación para actualizar una sucursal (PUT)
subsidiary_update_schema = swagger_auto_schema(
    operation_description="Actualiza una sucursal por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=SubsidiarySerializer,
    responses={
        200: SubsidiarySerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Sucursal no encontrada"),
    }
)

# Documentación para eliminar una sucursal (DELETE)
subsidiary_delete_schema = swagger_auto_schema(
    operation_description="Elimina una sucursal por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Sucursal eliminada con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Sucursal no encontrada"),
    }
)

# Documentación para obtener la lista de áreas (GET)
area_list_schema = swagger_auto_schema(
    operation_description="Lista todas las áreas registradas. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: AreaSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear una nueva área (POST)
area_create_schema = swagger_auto_schema(
    operation_description="Crea una nueva área. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=AreaSerializer,
    responses={
        201: AreaSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener un área por ID (GET)
area_detail_schema = swagger_auto_schema(
    operation_description="Obtiene un área específica por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: AreaSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Área no encontrada"),
    }
)

# Documentación para actualizar un área (PUT)
area_update_schema = swagger_auto_schema(
    operation_description="Actualiza un área por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=AreaSerializer,
    responses={
        200: AreaSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Área no encontrada"),
    }
)

# Documentación para eliminar un área (DELETE)
area_delete_schema = swagger_auto_schema(
    operation_description="Elimina un área por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Área eliminada con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Área no encontrada"),
    }
)


# Documentación para obtener la lista de departamentos (GET)
department_list_schema = swagger_auto_schema(
    operation_description="Lista todos los departamentos registrados. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: DepartmentSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear un nuevo departamento (POST)
department_create_schema = swagger_auto_schema(
    operation_description="Crea un nuevo departamento. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=DepartmentSerializer,
    responses={
        201: DepartmentSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener un departamento por ID (GET)
department_detail_schema = swagger_auto_schema(
    operation_description="Obtiene un departamento específico por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: DepartmentSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Departamento no encontrado"),
    }
)

# Documentación para actualizar un departamento (PUT)
department_update_schema = swagger_auto_schema(
    operation_description="Actualiza un departamento por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=DepartmentSerializer,
    responses={
        200: DepartmentSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Departamento no encontrado"),
    }
)

# Documentación para eliminar un departamento (DELETE)
department_delete_schema = swagger_auto_schema(
    operation_description="Elimina un departamento por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Departamento eliminado con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Departamento no encontrado"),
    }
)


# Documentación para obtener la lista de cargos (GET)
position_list_schema = swagger_auto_schema(
    operation_description="Lista todos los cargos registrados. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: PositionSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear un nuevo cargo (POST)
position_create_schema = swagger_auto_schema(
    operation_description="Crea un nuevo cargo. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=PositionSerializer,
    responses={
        201: PositionSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener un cargo por ID (GET)
position_detail_schema = swagger_auto_schema(
    operation_description="Obtiene un cargo específico por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: PositionSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Cargo no encontrado"),
    }
)

# Documentación para actualizar un cargo (PUT)
position_update_schema = swagger_auto_schema(
    operation_description="Actualiza un cargo por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=PositionSerializer,
    responses={
        200: PositionSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Cargo no encontrado"),
    }
)

# Documentación para eliminar un cargo (DELETE)
position_delete_schema = swagger_auto_schema(
    operation_description="Elimina un cargo por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Cargo eliminado con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Cargo no encontrado"),
    }
)


# Documentación para obtener la lista de centros de costo (GET)
center_cost_list_schema = swagger_auto_schema(
    operation_description="Lista todos los centros de costo registrados. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: CenterCostSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear un nuevo centro de costo (POST)
center_cost_create_schema = swagger_auto_schema(
    operation_description="Crea un nuevo centro de costo. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=CenterCostSerializer,
    responses={
        201: CenterCostSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener un centro de costo por ID (GET)
center_cost_detail_schema = swagger_auto_schema(
    operation_description="Obtiene un centro de costo específico por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: CenterCostSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Centro de costo no encontrado"),
    }
)

# Documentación para actualizar un centro de costo (PUT)
center_cost_update_schema = swagger_auto_schema(
    operation_description="Actualiza un centro de costo por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=CenterCostSerializer,
    responses={
        200: CenterCostSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Centro de costo no encontrado"),
    }
)

# Documentación para eliminar un centro de costo (DELETE)
center_cost_delete_schema = swagger_auto_schema(
    operation_description="Elimina un centro de costo por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Centro de costo eliminado con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Centro de costo no encontrado"),
    }
)


# Documentación para obtener la lista de entidades de salud (GET)
health_list_schema = swagger_auto_schema(
    operation_description="Lista todas las entidades de salud registradas. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: HealthSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear una nueva entidad de salud (POST)
health_create_schema = swagger_auto_schema(
    operation_description="Crea una nueva entidad de salud. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=HealthSerializer,
    responses={
        201: HealthSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener una entidad de salud por ID (GET)
health_detail_schema = swagger_auto_schema(
    operation_description="Obtiene una entidad de salud específica por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: HealthSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Entidad de salud no encontrada"),
    }
)

# Documentación para actualizar una entidad de salud (PUT)
health_update_schema = swagger_auto_schema(
    operation_description="Actualiza una entidad de salud por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=HealthSerializer,
    responses={
        200: HealthSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Entidad de salud no encontrada"),
    }
)

# Documentación para eliminar una entidad de salud (DELETE)
health_delete_schema = swagger_auto_schema(
    operation_description="Elimina una entidad de salud por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Entidad de salud eliminada con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Entidad de salud no encontrada"),
    }
)


# Documentación para obtener la lista de AFP (GET)
afp_list_schema = swagger_auto_schema(
    operation_description="Lista todas las AFP registradas. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: AfpSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear una nueva AFP (POST)
afp_create_schema = swagger_auto_schema(
    operation_description="Crea una nueva AFP. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=AfpSerializer,
    responses={
        201: AfpSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener una AFP por ID (GET)
afp_detail_schema = swagger_auto_schema(
    operation_description="Obtiene una AFP específica por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: AfpSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("AFP no encontrada"),
    }
)

# Documentación para actualizar una AFP (PUT)
afp_update_schema = swagger_auto_schema(
    operation_description="Actualiza una AFP por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=AfpSerializer,
    responses={
        200: AfpSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("AFP no encontrada"),
    }
)

# Documentación para eliminar una AFP (DELETE)
afp_delete_schema = swagger_auto_schema(
    operation_description="Elimina una AFP por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("AFP eliminada con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("AFP no encontrada"),
    }
)


# Documentación para obtener la lista de instituciones APV (GET)
institutions_apv_list_schema = swagger_auto_schema(
    operation_description="Lista todas las instituciones APV registradas. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: InstitutionsApvSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear una nueva institución APV (POST)
institutions_apv_create_schema = swagger_auto_schema(
    operation_description="Crea una nueva institución APV. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=InstitutionsApvSerializer,
    responses={
        201: InstitutionsApvSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener una institución APV por ID (GET)
institutions_apv_detail_schema = swagger_auto_schema(
    operation_description="Obtiene una institución APV específica por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: InstitutionsApvSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Institución APV no encontrada"),
    }
)

# Documentación para actualizar una institución APV (PUT)
institutions_apv_update_schema = swagger_auto_schema(
    operation_description="Actualiza una institución APV por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=InstitutionsApvSerializer,
    responses={
        200: InstitutionsApvSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Institución APV no encontrada"),
    }
)

# Documentación para eliminar una institución APV (DELETE)
institutions_apv_delete_schema = swagger_auto_schema(
    operation_description="Elimina una institución APV por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Institución APV eliminada con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Institución APV no encontrada"),
    }
)


# Documentación para obtener la lista de bancos (GET)
bank_list_schema = swagger_auto_schema(
    operation_description="Lista todos los bancos registrados. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: BankSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear un nuevo banco (POST)
bank_create_schema = swagger_auto_schema(
    operation_description="Crea un nuevo banco. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=BankSerializer,
    responses={
        201: BankSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener un banco por ID (GET)
bank_detail_schema = swagger_auto_schema(
    operation_description="Obtiene un banco específico por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: BankSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Banco no encontrado"),
    }
)

# Documentación para actualizar un banco (PUT)
bank_update_schema = swagger_auto_schema(
    operation_description="Actualiza un banco por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=BankSerializer,
    responses={
        200: BankSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Banco no encontrado"),
    }
)

# Documentación para eliminar un banco (DELETE)
bank_delete_schema = swagger_auto_schema(
    operation_description="Elimina un banco por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Banco eliminado con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Banco no encontrado"),
    }
)