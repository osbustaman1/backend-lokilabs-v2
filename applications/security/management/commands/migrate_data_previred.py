import json

from django.core.management.base import BaseCommand
from django.db import connections
from applications.company.models import Afp
from applications.humanresources.models import MonthlyPreviredData
from applications.security.models import Customers
from daemon_previred import get_data_previred
from remunerations.data_bases import load_data_base

class Command(BaseCommand):
    help = 'Se inicia la migracion para todas las bases de datos'

    def handle(self, *args, **options):

        load_data_base()

        lista = Customers.objects.all()

        for base in lista:
            nombre_bd = base.cus_name_bd
            data_previred = get_data_previred()
            dataPrevired = MonthlyPreviredData()
            dataPrevired.dpm_json = data_previred
            dataPrevired.save(using=nombre_bd)

            # Truncate the table in the specific database
            # with connections[nombre_bd].cursor() as cursor:
            #     cursor.execute(f'TRUNCATE TABLE {Afp._meta.db_table}')

            self.stdout.write(f'Los indicadores Previred para el cliente {base.cus_name} fueron migrados con exito!')



        self.stdout.write('¡La migracion para todas las bases de datos fue realizada con exito!')