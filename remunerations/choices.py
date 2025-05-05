YES_NO_OPTIONS = (
    ('Y', 'YES'),
    ('N', 'NO'),
)

TYPE_INSTITUTIONS = (
    (1, 'BANCO'),
    (2, 'AFP'),
)


TYPE_CONTRACT = (
    (1, 'Contrato'),
    (2, 'Anexo'),
)

CLASSIFICATION = (
    (1, 'Haberes'),
    (2, 'Descuentos'),
)

TYPE_CLASSIFICATION = (
    (1, 'Imponible'),
    (2, 'No Imponible'),
    (3, 'Previsional'),
    (4, 'Judicial'),
    (5, 'Tributario'),
    (6, 'Acordado')
)

SEARCH_FIELDS = (
    ('0', ' --------- '),
    ('ISAPRE', 'isapre'),
    ('FONASA', 'fonasa'),
    ('AFP', 'afp'),
)

REMUNERATION_TYPE = (
    (0, ' --------- '),
    (1, 'Sueldo'),
    (2, 'Sobresueldo'),
    (3, 'Variable'),
    (4, 'Eventuales'),
    (5, 'Gratificación'),
    (6, 'Descuento')
)

TITLES = (
    (0, ' --------- '),
    (1, 'RENTAS TOPES IMPONIBLES'),
    (2, 'RENTAS MÍNIMAS IMPONIBLES'),
    (3, 'AHORRO PREVISIONAL VOLUNTARIO (APV)'),
    (4, 'DEPÓSITO CONVENIDO'),
)

TYPE_VARIABLE = (
    (0, ' --------- '),
    (1, 'PREVIRED'),
    (2, 'REMUNERACIONES'),
)

SEX_OPTIONS = (
    ('M', 'MASCULINO'),
    ('F', 'FEMENINO'),
)

CIVIL_STATUS_OPTIONS = (
    (1, 'Solter@'),
    (2, 'Casad@'),
    (3, 'Divorciad@'),
    (4, 'Viud@'),
    (5, 'No informa'),
)

TYPE_USERS = (
    (1, 'Super-Admin'),
    (2, 'Recursos Humanos'),
    (3, 'Recursos Humanos Administrador'),
    (4, 'Jefatura'),
    (5, 'Colaborador'),
)

PAYMENT_METHOD_OPTIONS = (
    (1, 'Depósito en cuenta'),
    (2, 'Cheque'),
    (3, 'Transferencia'),
    (4, 'Efectivo'),
)

BANK_ACCOUNT_TYPE_OPTIONS = (
    (1, 'Cuenta Vista'),
    (2, 'Cuenta de Ahorro'),
    (3, 'Cuenta Bancaria para Estudiante'),
    (4, 'Cuenta Chequera Electrónica'),
    (5, 'Cuenta Rut'),
    (6, 'Cuenta Bancaria para Extranjeros'),
    (7, 'Cuenta Corriente'),
)

STUDY_TYPE_OPTIONS = (
    (1, 'Enseñanza Media'),
    (2, 'Estudios Superiores (CFT)'),
    (3, 'Estudios Universitarios'),
)

STUDY_STATUS_OPTIONS = (
    (1, 'Completo'),
    (2, 'Incompleto'),
    (3, 'Abandonado'),
)

WORKER_TYPE = (
    (0, '[seleccione]'),
    (1, 'Activo (no pensionado)'),
    (2, 'Pensionado y cotiza AFP'),
    (3, 'Pensionado y no cotiza AFP'),
    (4, 'Activo mayor de 65 años (nunca pensionado)'),
)

OPCIONES = (
    ('S', 'SI'),
    ('N', 'NO'),
)

NOTIFICATION = (
    ('E', 'Email'),
    ('C', 'Carta'),
)

AMOUNT_TYPE = (
    ('P', 'Porcentaje'),
    ('M', 'Monto'),
)

TYPE_GRATIFICATION = (
    ('A', 'Anual'),
    ('M', 'Mensual'),
)

CONTRACT_TYPE = (
    (1, 'Plazo Indefinido'),
    (2, 'Plazo Fijo'),
    (3, 'Plazo Indefinido 11 años o más'),
    (4, 'Trabajador de Casa Particular'),
)

FAMILY_ALLOWANCE_SECTION = (
    (0, '---------'),
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (4, 'D'),
)

ESTATE_JOB = (
    (0, '[seleccione]'),
    (1, 'Vigente'),
    (2, 'Desvinculado')
)

CONTRIBUTION_TYPE = (
    (0, '---------'),
    (1, 'PESOS ($)'),
    (2, 'PORCENTAJE (%)'),
    (3, 'UNIDAD DE FOMENTO (UF)'),
)

TAX_REGIME = (
    (0, '---------'),
    (1, 'APV Regimen A'),
    (2, 'APV Regimen B'),
    (3, 'Depósitos Convenidos(**)'),
)

SHAPE = (
    (0, '---------'),
    (1, 'DIRECTA'),
    (2, 'INDIRECTA'),
)

WORKER_SECTOR = (
    (0, '[seleccione]'),
    (1, 'Público'),
    (2, 'Privado'),
)

TYPE_OF_WORK_DAYS = (
    (1, 'Ordinarias'),
    (2, 'Extraordinarias'),
)

ALL_DAYS = (
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miércoles', 'Miércoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sábado', 'Sábado'),
    ('Domingo', 'Domingo'),
)

HEALTH_ENTITY_TYPE = (
    ('F', 'FONASA'),
    ('I', 'ISAPRE'),
)


APVI = (
    (1, 'Cotizaciones Voluntarias'),
    (2, 'Deposito Ahorro Previsional Voluntario'),
    (3, 'Deposito Convenio')
)

TYPE_PLAN_APV = (
    (1, 'UF'),
    (2, 'PESOS')
)


PAYMENT_TYPE_APV = (
    (1, 'DIRECTO'),
    (2, 'INDIRECTO')
)

REGIMENT_TYPE_APV = (
    (1, 'Regimen A'),
    (2, 'Regimen B')
)


HEAVY_WORK_PERCENTAGE = (
    (0, 'No tiene trabajo pesado'),
    (1, 'Trabajo Pesado 2%'),
    (2, 'Trabajo Menos Pesado 4%')
)


TYPE_OF_WORK_MODES = (
    (1, 'Trabajo con horario fijo o jornada ordinaria'),
    (2, 'Trabajo sin horario (Artículo 22 del Código del Trabajo)'),
    (3, 'Trabajo presencial'),
    (4, 'Teletrabajo o trabajo a distancia'),
    (5, 'Trabajo por turnos (rotativos, fijos, nocturnos, etc.)'),
    (6, 'Trabajo con jornada parcial'),
    (7, 'Trabajo por temporada o eventual'),
    (8, 'Trabajo en plataformas digitales'),
    (9, 'Trabajo por obra o faena'),
    (10, 'Trabajo freelance o independiente (con boletas de honorarios)'),
    (11, 'Trabajo en régimen de subcontratación'),
    (12, 'Trabajo a tiempo parcial juvenil (para estudiantes entre 18 y 28 años)'),
    (13, 'Trabajo híbrido (combinación de presencial y teletrabajo)'),
    (14, 'Trabajo doméstico'),
    (15, 'Prácticas profesionales'),
    (16, 'Trabajo en régimen especial para personas con discapacidad'),
    (17, 'Trabajo voluntario'),
    (18, 'Trabajo asociado a cooperativas (régimen especial para cooperativas)'),
    (19, 'Trabajo en régimen de aprendizaje (aprendices o programas formativos)'),
    (20, 'Trabajo en régimen de servicios transitorios (contratos por empresas de servicios transitorios)'),
)

ESTATE_VACATION = (
    (1, 'Pendiente'),
    (2, 'Aprobado'),
    (3, 'Rechazado'),
)


TYPE_VACATION = (
    (1, 'Normales'),
    (2, 'Progresivas'),
    (3, 'Adicionales'),
)



def elige_choices(choices, elegir):
    value = ''
    for l in choices:
        if l[0] == elegir:
            value = l[1]
    return value