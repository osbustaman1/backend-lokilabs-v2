from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from applications.security.api.serializer import ListItemsSerializer, ListSubItemsSerializer, MenuItemsSerializer, MenuSerializer


jwt_header = openapi.Parameter(
    'token',
    openapi.IN_HEADER,
    description="Token de autenticación JWT",
    type=openapi.TYPE_STRING,
    required=True
)

# Documentación para obtener la lista de menús (GET)
menu_list_schema = swagger_auto_schema(
    operation_description="Lista todos los menús registrados. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: MenuSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear un nuevo menú (POST)
menu_create_schema = swagger_auto_schema(
    operation_description="Crea un nuevo menú. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=MenuSerializer,
    responses={
        201: MenuSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para obtener un menú por ID (GET)
menu_detail_schema = swagger_auto_schema(
    operation_description="Obtiene un menú específico por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: MenuSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Menú no encontrado"),
    }
)

# Documentación para actualizar un menú (PUT)
menu_update_schema = swagger_auto_schema(
    operation_description="Actualiza un menú por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    request_body=MenuSerializer,
    responses={
        200: MenuSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Menú no encontrado"),
    }
)

# Documentación para eliminar un menú (DELETE)
menu_delete_schema = swagger_auto_schema(
    operation_description="Elimina un menú por ID. Se requiere un token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Menú eliminado con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Menú no encontrado"),
    }
)


# Documentación para obtener lista de ítems de menú (GET)
listitems_list_schema = swagger_auto_schema(
    operation_description="Lista todos los ítems de menú registrados. Requiere token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: ListItemsSerializer(many=True),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para crear ítem de menú (POST)
listitems_create_schema = swagger_auto_schema(
    operation_description="Crea nuevo ítem de menú. Requiere token JWT.",
    manual_parameters=[jwt_header],
    request_body=ListItemsSerializer,
    responses={
        201: ListItemsSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
    }
)

# Documentación para detalle de ítem (GET)
listitems_detail_schema = swagger_auto_schema(
    operation_description="Obtiene un ítem de menú específico por ID. Requiere token JWT.",
    manual_parameters=[jwt_header],
    responses={
        200: ListItemsSerializer,
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Ítem no encontrado"),
    }
)

# Documentación para actualizar ítem (PUT)
listitems_update_schema = swagger_auto_schema(
    operation_description="Actualiza un ítem de menú por ID. Requiere token JWT.",
    manual_parameters=[jwt_header],
    request_body=ListItemsSerializer,
    responses={
        200: ListItemsSerializer,
        400: openapi.Response("Error en la solicitud"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Ítem no encontrado"),
    }
)

# Documentación para eliminar ítem (DELETE)
listitems_delete_schema = swagger_auto_schema(
    operation_description="Elimina un ítem de menú por ID. Requiere token JWT.",
    manual_parameters=[jwt_header],
    responses={
        204: openapi.Response("Ítem eliminado con éxito"),
        401: openapi.Response("Unauthorized"),
        404: openapi.Response("Ítem no encontrado"),
    }
)


# Documentación para obtener subitems de menú (GET)
listsubitems_list_schema = swagger_auto_schema(
    operation_description="Lista todos los subitems de menú. Requiere JWT",
    manual_parameters=[jwt_header],
    responses={200: ListSubItemsSerializer(many=True), 401: "Unauthorized"}
)

# Crear subitem (POST)
listsubitems_create_schema = swagger_auto_schema(
    operation_description="Crea nuevo subitem de menú. Requiere JWT",
    request_body=ListSubItemsSerializer,
    responses={201: ListSubItemsSerializer, 400: "Bad Request", 401: "Unauthorized"}
)

# Detalle de subitem (GET)
listsubitems_detail_schema = swagger_auto_schema(
    operation_description="Obtiene un subitem por ID. Requiere JWT",
    responses={200: ListSubItemsSerializer, 404: "No encontrado", 401: "Unauthorized"}
)

# Actualizar subitem (PUT)
listsubitems_update_schema = swagger_auto_schema(
    operation_description="Actualiza subitem completo. Requiere JWT",
    request_body=ListSubItemsSerializer,
    responses={200: ListSubItemsSerializer, 400: "Bad Request", 401: "Unauthorized"}
)

# Eliminar subitem (DELETE)
listsubitems_delete_schema = swagger_auto_schema(
    operation_description="Elimina subitem por ID. Requiere JWT",
    responses={204: "Eliminado", 401: "Unauthorized", 404: "No encontrado"}
)


# Documentación para relaciones menú-ítems (GET)
menuitems_list_schema = swagger_auto_schema(
    operation_description="Lista todas las relaciones menú-ítems. Requiere JWT",
    manual_parameters=[jwt_header],
    responses={200: MenuItemsSerializer(many=True), 401: "Unauthorized"}
)

# Crear relación (POST)
menuitems_create_schema = swagger_auto_schema(
    operation_description="Crea nueva relación menú-ítem. Requiere JWT",
    request_body=MenuItemsSerializer,
    responses={201: MenuItemsSerializer, 400: "Bad Request", 401: "Unauthorized"}
)

# Detalle de relación (GET)
menuitems_detail_schema = swagger_auto_schema(
    operation_description="Obtiene relación específica por ID. Requiere JWT",
    responses={200: MenuItemsSerializer, 404: "No encontrado", 401: "Unauthorized"}
)

# Actualizar relación (PUT)
menuitems_update_schema = swagger_auto_schema(
    operation_description="Actualiza relación completa. Requiere JWT",
    request_body=MenuItemsSerializer,
    responses={200: MenuItemsSerializer, 400: "Bad Request", 401: "Unauthorized"}
)

# Eliminar relación (DELETE)
menuitems_delete_schema = swagger_auto_schema(
    operation_description="Elimina relación por ID. Requiere JWT",
    responses={204: "Eliminado", 401: "Unauthorized", 404: "No encontrado"}
)