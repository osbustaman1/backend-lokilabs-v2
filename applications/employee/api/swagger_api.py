from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from applications.employee.api.serializer import EmployeeSerializer, ListUserCompanySerializer, UserCompanySerializer, UserTypeContractSerializer

jwt_header = openapi.Parameter(
    'token',
    openapi.IN_HEADER,
    description="Token de autenticación JWT",
    type=openapi.TYPE_STRING,
    required=True
)

# Documentación para obtener lista de empleados (GET)
employee_list_schema = swagger_auto_schema(
    operation_description="Lista todos los empleados registrados. Requiere token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: EmployeeSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear empleado (POST)
employee_create_schema = swagger_auto_schema(
    operation_description="Crea un nuevo empleado. Requiere token JWT.",
    manual_parameters=[jwt_header],
    request_body=EmployeeSerializer,
    responses={
        201: EmployeeSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para detalle de empleado (GET)
employee_detail_schema = swagger_auto_schema(
    operation_description="Obtiene un empleado específico por ID y por ID de empresa. Requiere token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: EmployeeSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Empleado no encontrado"),
    }
)

# Documentación para actualizar empleado (PUT)
employee_update_schema = swagger_auto_schema(
    operation_description="Actualiza un empleado por ID. Requiere token JWT.",
    manual_parameters=[jwt_header],
    request_body=EmployeeSerializer,
    responses={
        200: EmployeeSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Empleado no encontrado"),
    }
)

# Documentación para eliminar empleado (DELETE)
employee_delete_schema = swagger_auto_schema(
    operation_description="Elimina un empleado por ID. Requiere token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Empleado eliminado con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Empleado no encontrado"),
    }
)

# Documentación para obtener lista de relaciones usuario-empresa (GET)
user_company_list_schema = swagger_auto_schema(
    operation_description="Lista todas las relaciones usuario-empresa. Requiere token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: UserCompanySerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear relación (POST)
user_company_create_schema = swagger_auto_schema(
    operation_description="Crea nueva relación usuario-empresa. Requiere token JWT.",
    manual_parameters=[jwt_header],
    request_body=UserCompanySerializer,
    responses={
        201: UserCompanySerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para detalle de relación (GET)
user_company_detail_schema = swagger_auto_schema(
    operation_description="Obtiene relación específica por ID. Requiere token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: UserCompanySerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Relación no encontrada"),
    }
)

# Documentación para actualizar relación (PUT)
user_company_update_schema = swagger_auto_schema(
    operation_description="Actualiza relación por ID. Requiere token JWT.",
    manual_parameters=[jwt_header],
    request_body=UserCompanySerializer,
    responses={
        200: UserCompanySerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Relación no encontrada"),
    }
)

# Documentación para eliminar relación (DELETE)
user_company_delete_schema = swagger_auto_schema(
    operation_description="Elimina relación por ID. Requiere token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Relación eliminada con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Relación no encontrada"),
    }
)


# Documentación para obtener la lista de contratos de usuario (GET)
user_type_contract_list_schema = swagger_auto_schema(
    operation_description="Lista todos los contratos de usuario registrados. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: UserTypeContractSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear un nuevo contrato (POST)
user_type_contract_create_schema = swagger_auto_schema(
    operation_description="Crea un nuevo contrato de usuario. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=UserTypeContractSerializer,
    responses={
        201: UserTypeContractSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener un contrato por ID (GET)
user_type_contract_detail_schema = swagger_auto_schema(
    operation_description="Obtiene un contrato específico por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: UserTypeContractSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Contrato no encontrado"),
    }
)

# Documentación para actualizar un contrato (PUT)
user_type_contract_update_schema = swagger_auto_schema(
    operation_description="Actualiza un contrato por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=UserTypeContractSerializer,
    responses={
        200: UserTypeContractSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Contrato no encontrado"),
    }
)

# Documentación para eliminar un contrato (DELETE)
user_type_contract_delete_schema = swagger_auto_schema(
    operation_description="Elimina un contrato por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Contrato eliminado con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Contrato no encontrado"),
    }
)

# Documentación para obtener lista de usuarios (GET)
user_list_schema = swagger_auto_schema(
    operation_description="Lista todos los usuarios con información adicional de Employee y UserCompany. Requiere token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: ListUserCompanySerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)