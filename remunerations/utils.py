import boto3
import datetime
import re
import pandas as pd
import pdfkit
import base64

from jwt import encode, decode, ExpiredSignatureError, InvalidSignatureError
from requests import request
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from django.conf import settings
from decouple import config
from urllib.parse import urlparse
from django.template.loader import get_template

from pathlib import Path

import mailtrap as mt

from remunerations.settings.base import WKHTMLTOPDF_BIN_PATH

# Lista negra para almacenar tokens revocados
blacklist = set()

def expire_date(days: int):
    now = datetime.datetime.now()
    new_date = now + datetime.timedelta(days)
    return new_date

def write_token(data: dict):
    refresh = RefreshToken()
    token = encode(payload={**data, 'exp': expire_date(int(config('EXPIRE_DATE'))), 'jti': str(refresh.access_token)}, key=config('SECRET_KEY'), algorithm='HS256')
    return token.encode('UTF-8')

def decode_token(token: str):
    try:
        # Verificar si el token está en la lista negra
        if token in blacklist:
            return None

        decoded_token = decode(token, key=config('SECRET_KEY'), algorithms=['HS256'])
        return decoded_token
    except ExpiredSignatureError:
        # Manejar error de token expirado
        return None
    except InvalidSignatureError:
        # Manejar error de token inválido
        return None

def revoke_token(token: str):
    try:
        # Crear un objeto RefreshToken
        refresh_token = RefreshToken(token)
        
        # Verificar que el token es de tipo refresh
        if refresh_token.token_type != 'refresh':
            raise ValueError('El token no es de tipo refresh')

        # Obtener o crear el OutstandingToken
        outstanding_token, created = OutstandingToken.objects.get_or_create(
            jti=refresh_token['jti'],
            defaults={
                'token': str(refresh_token),
                'user': refresh_token['user'],
                'created_at': datetime.datetime.now(),
                'expires_at': refresh_token['exp']
            }
        )

        # Añadir el OutstandingToken a la lista negra
        BlacklistedToken.objects.create(token=outstanding_token)
        return {
            'message': 'Token revocado con éxito',
            'success': True
        }
    except Exception as e:
        return {
            'message': f'Error revoking token: {e}',
            'success': False
        }
    
def validarRut(rut):
    rut = rut.replace(".", "").replace("-", "")  # Eliminar puntos y guiones
    if not re.match(r'^\d{1,8}[0-9K]$', rut):  # Verificar formato
        return False
    rut_sin_dv = rut[:-1]
    dv = rut[-1].upper()  # Obtener dígito verificador
    multiplicador = 2
    suma = 0
    for r in reversed(rut_sin_dv):
        suma += int(r) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    resto = suma % 11
    dv_calculado = 11 - resto
    if dv_calculado == 11:
        dv_calculado = '0'
    elif dv_calculado == 10:
        dv_calculado = 'K'
    else:
        dv_calculado = str(dv_calculado)
    return dv == dv_calculado


def get_subdomain():
    parsed_url = urlparse(request.build_absolute_uri())
    hostname = parsed_url.hostname
    subdomain = hostname.split('.')[0] if hostname else None
    return subdomain


def create_folder(cus_name_bd):
    # Inicializar el cliente de S3 con las credenciales de AWS
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )

    # Nombre del bucket
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    # Crear una "carpeta" (un directorio vacío) en el bucket de S3
    directory_name = f"customers/{cus_name_bd}/"

    # Verificar si el directorio ya existe
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory_name, MaxKeys=1)

    # Si ya existe, no hacer nada
    if 'Contents' in response:
        print(f"Directory '{directory_name}' already exists in bucket '{bucket_name}'")
        return directory_name 

    # Si no existe, crear el directorio
    s3.put_object(Bucket=bucket_name, Key=directory_name)

    print(f"Directory '{directory_name}' created in bucket '{bucket_name}'")
    return directory_name


def create_folder_collaborator(cus_name_bd, user_id):
    # Inicializar el cliente de S3 con las credenciales de AWS
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )

    # Nombre del bucket
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    # Crear una "carpeta" (un directorio vacío) en el bucket de S3
    directory_name = f"customers/{cus_name_bd}/{user_id}/"

    # Verificar si el directorio ya existe
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory_name, MaxKeys=1)

    # Si ya existe, no hacer nada
    if 'Contents' in response:
        print(f"Directory '{directory_name}' already exists in bucket '{bucket_name}'")
        return directory_name 

    # Si no existe, crear el directorio
    s3.put_object(Bucket=bucket_name, Key=directory_name)

    print(f"Directory '{directory_name}' created in bucket '{bucket_name}'")
    return directory_name


def upload_file_to_s3(file_path, directory_name, file_name):
    """
    Sube un archivo a un directorio específico en un bucket de S3.

    :param file_path: Ruta local del archivo a subir.
    :param directory_name: Nombre del directorio en el bucket de S3.
    :param file_name: Nombre del archivo en el bucket de S3.
    :return: URL del archivo subido.
    """
    # Inicializar el cliente de S3 con las credenciales de AWS
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )

    # Ruta completa en el bucket de S3
    s3_path = f"{directory_name}/{file_name}"

    try:
        # Subir el archivo
        s3.upload_file(file_path, settings.BUCKET_NAME, s3_path)
        print(f"File '{file_name}' uploaded to '{s3_path}' in bucket '{settings.BUCKET_NAME}'")

        # Obtener la URL del archivo subido2
        file_url = f"https://{settings.BUCKET_NAME}.s3.amazonaws.com/{s3_path}"
        return file_url
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None
    

def generate_pdf(html, isTemplate = False, name_template = False, data = {}):
    
    options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
        }

    pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_BIN_PATH)

    if isTemplate:
        file_template = f'pdf/{name_template}'
        template = get_template(file_template)
        html = template.render(data)

    pdf = pdfkit.from_string(html, False, options=options, configuration=pdfkit_config)
    pdf_base64 = base64.b64encode(pdf).decode('utf-8')

    return pdf_base64


def send_email(data_email):
    """
    Envía un correo electrónico utilizando Mailtrap.
    
    Parámetros:
        data_email (dict): Un diccionario con la información del correo, incluyendo opcionalmente archivos adjuntos e imágenes inline.
    """

    # Construcción del correo con los datos esenciales
    mail = mt.Mail(
        sender=mt.Address(email=data_email['sender'][0]['email'], name=data_email['sender'][0]['name']),
        to=[mt.Address(email=recipient['email'], name=recipient['name']) for recipient in data_email.get('to', [])],
        cc=[mt.Address(email=cc['email'], name=cc['name']) for cc in data_email.get('cc', [])] if 'cc' in data_email else None,
        bcc=[mt.Address(email=bcc['email'], name=bcc['name']) for bcc in data_email.get('bcc', [])] if 'bcc' in data_email else None,
        subject=data_email['subject'],
        text=data_email.get('text', ''),
        html=data_email.get('html', ''),
        category=data_email.get('category', ''),
        headers={"X-MT-Header": "Custom header"},
        custom_variables={"year": 2023},
    )

    # Agregar imágenes inline si existen
    if 'inline_attachments' in data_email:
        for inline in data_email['inline_attachments']:
            try:
                mail.attachments.append(
                    mt.Attachment(
                        content=inline['content'],
                        filename=inline['filename'],
                        disposition=mt.Disposition.INLINE,
                        mimetype=inline['mimetype'],
                        content_id=inline.get('content_id', inline['filename']),
                    )
                )
            except Exception as e:
                print(f"Error al procesar la imagen inline {inline['filename']}: {e}")

    # Agregar archivos adjuntos si existen
    if 'attachments' in data_email:
        for attachment in data_email['attachments']:
            try:
                mail.attachments.append(
                    mt.Attachment(
                        content=attachment['content'],
                        filename=attachment['filename'],
                        disposition=mt.Disposition.ATTACHMENT,
                        mimetype=attachment['mimetype'],
                    )
                )
            except Exception as e:
                print(f"Error al procesar el archivo adjunto {attachment['filename']}: {e}")

    # Enviar correo
    client = mt.MailtrapClient(token="8490f930a7d516238a2d07e3b2cf408b")
    client.send(mail)
