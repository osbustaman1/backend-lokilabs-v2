import datetime
import json
import requests
from lxml import html

from indicator_economic import IndicatorEconomic


page = requests.get('https://www.previred.com/indicadores-previsionales/')


def obtener_valor(cadena, separador_uno, separador_dos):

    tree = html.fromstring(page.content)  
    xpath_cadena = tree.xpath(f"{cadena}/text()")[0]
    return float((((xpath_cadena.split(separador_uno)[0]).split(separador_dos)[0]).replace(",","."))[:-1])

def de_string_float_porcentaje(texto_numero):
    numero = float(texto_numero.replace(",",".")[:-1])
    return numero

def translate_month(month, language = 'es_cl'):
    """
    translate_month - Funcion obtiene el mes en español

    :param month: mes a consultar
    :param language: lenguaje a traducir, por defecto es en español chileno
    :return: 
        translation retorna el mes consultado
    """

    idioms = {
        'es_cl': {
            'january': 'enero',
            'february': 'febrero',
            'march': 'marzo',
            'april': 'abril',
            'may': 'mayo',
            'june': 'junio',
            'july': 'julio',
            'august': 'agosto',
            'september': 'septiembre',
            'october': 'octubre',
            'november': 'noviembre',
            'december': 'diciembre',
        }
    }

    month_lower = month.lower()
    translation = idioms.get(language, {}).get(month_lower, month)

    return translation



def get_data_previred():

    list_variables = []

    if page.status_code == 200:
        # Obtiene la fecha y hora actual
        fecha_actual = datetime.datetime.now()
        year = fecha_actual.year
        month = fecha_actual.month

        uf_presente_mes = IndicatorEconomic.get_uf_value_last_day()
        valor_uf = float(uf_presente_mes['Valor'].replace('.', '').replace(',', '.'))

        utm_presente_mes = IndicatorEconomic.get_utm()
        if "CodigoError" in utm_presente_mes and (utm_presente_mes["CodigoError"] == 81):
            utm_presente_mes = IndicatorEconomic.get_utm_year_month(year, (month - 1))

        valor_utm = float(utm_presente_mes['Valor'].replace('.', '').replace(',', '.'))

        tree = html.fromstring(page.content)  

        list_variables.append({
            "key":1, 
            "title": "Valores UF, UTM y UTA",
            "short_title": "uf_utm_uta",
            "data": [
                {
                    "name": f"Valor UF",
                    "value": valor_uf,
                },{
                    "name": f"Valor UTM",
                    "value": valor_utm,
                },{
                    "name": f"Valor UTA",
                    "value": valor_utm * 12,
                }
            ]
        })

        # Get element using XPath
        xpath_afiliados_afp = tree.xpath('//*[@id="p_p_id_56_INSTANCE_KQr4e6mJcSti_"]/div/div/div[1]/table/tbody/tr[2]/td[1]/text()')[0]
        tope_afiliados_afp = float(((xpath_afiliados_afp.split("(")[1]).split(" ")[0]).replace(",","."))

        xpath_afiliados_ips = tree.xpath('//*[@id="p_p_id_56_INSTANCE_KQr4e6mJcSti_"]/div/div/div[1]/table/tbody/tr[3]/td[1]/text()')[0]
        tope_afiliados_ips = float(((xpath_afiliados_ips.split(") (")[1]).split(" ")[0]).replace(",","."))

        xpath_afiliados_cesantia = tree.xpath('//*[@id="p_p_id_56_INSTANCE_KQr4e6mJcSti_"]/div/div/div[1]/table/tbody/tr[4]/td[1]/text()')[0]
        tope_afiliados_cesantia = float(((xpath_afiliados_cesantia.split("(")[1]).split(" ")[0]).replace(",","."))

        list_variables.append({
            "key": 2, 
            "title": "Renta topes imponibles",
            "short_title": "previson_topes_imponibles",
            "data": [
                {
                    "name": f"Para afiliados a una AFP ({tope_afiliados_afp} UF)",
                    "value": int(round((tope_afiliados_afp * valor_uf), 0)),
                },{
                    "name": f"Para afiliados al IPS (ex INP) ({tope_afiliados_ips} UF)",
                    "value": int(round((tope_afiliados_ips * valor_uf), 0)),
                },{
                    "name": f"Para Seguro de Cesantía ({tope_afiliados_cesantia} UF)",
                    "value": int(round((tope_afiliados_cesantia * valor_uf), 0)),
                }
            ]
        })


        """
        **************************************************
        RENTAS MÍNIMAS IMPONIBLES
        **************************************************
        """

        # Utiliza el XPath para obtener la tabla
        xpath_afp_capital = '//*[@id="p_p_id_56_INSTANCE_z00IZRTURtAo_"]/div/div/div[1]/table'
        tabla = tree.xpath(xpath_afp_capital)

        # Asegúrate de que se haya encontrado la tabla
        if tabla:
            # Selecciona todos los elementos 'tr' dentro de la tabla
            tr_elementos = tabla[0].xpath('.//tr')

            # Inicializa la lista de filas
            filas = []
            list_data_rentas_minimas_imponibles = []
            for tr in tr_elementos:
                # Selecciona todos los elementos 'td' dentro de la fila que no tienen la clase 'encabezado_tabla_ind'
                td_elementos = tr.xpath('.//td[not(@class="encabezado_tabla_ind")]')
                fila = [td.text_content().strip() for td in td_elementos]

                # Agrega la fila a la lista de filas
                if fila:
                    filas.append(fila)

            # Imprime las filas
            for fila in filas:
                valor = int((fila[1].split(" ")[1]).replace(".", ""))
                list_data_rentas_minimas_imponibles.append({
                    "name": fila[0],
                    "value": valor,
                })

            list_variables.append({
                "key": 3, 
                "title": "Rentas mínimas imponibles",
                "short_title": "rentas_minimas_imponibles",
                "data": list_data_rentas_minimas_imponibles
            })

        else:
            print("No se encontró la tabla con el XPath proporcionado.")


        
        """
        **************************************************
        AHORRO PREVISIONAL VOLUNTARIO (APV)
        **************************************************
        """

        xpath_ahorro_previsional_mensual = tree.xpath('//*[@id="p_p_id_56_INSTANCE_3WYryRoUZVvN_"]/div/div/div[1]/table/tbody/tr[2]/td[1]/text()')[0]
        ahorro_previsional_mensual = float(((xpath_ahorro_previsional_mensual.split("(")[1]).split(" ")[0]).replace(",","."))

        xpath_ahorro_previsional_anual = tree.xpath('//*[@id="p_p_id_56_INSTANCE_3WYryRoUZVvN_"]/div/div/div[1]/table/tbody/tr[3]/td[1]/text()')[0]
        ahorro_previsional_anual = float(((xpath_ahorro_previsional_anual.split("(")[1]).split(" ")[0]).replace(",","."))

        list_variables.append({
            "key": 4, 
            "title": "Ahorro previsional voluntario (APV)",
            "short_title": "tope_apv",
            "data": [
                    {
                        "name": f"Tope Mensual ({ahorro_previsional_mensual} UF)",
                        "value": int(round((ahorro_previsional_mensual * valor_uf), 0)),
                    },{
                        "name": f"Tope Anual ({ahorro_previsional_anual} UF)",
                        "value": int(round((ahorro_previsional_anual * valor_uf), 0)),
                    }
                ]
            })
        


        """
        **************************************************
        DEPÓSITO CONVENIDO
        **************************************************
        """

        xpath_deposito_convenido = tree.xpath('//*[@id="p_p_id_56_INSTANCE_4jdY7Es6TfZ9_"]/div/div/div[1]/table/tbody/tr[2]/td[1]/text()')[0]
        deposito_convenido = float(((xpath_deposito_convenido.split("(")[1]).split(" ")[0]).replace(",","."))

        list_variables.append({
            "key": 5, 
            "title": "Deposito convenido",
            "short_title": "tope_deposito_convenio",
            "data": [{
                "name": f"Tope anual ({deposito_convenido} UF)",
                "value": int(round((deposito_convenido * valor_uf), 0)),
            }]
        })


        """
        **************************************************
        SEGURO DE CESANTÍA
        **************************************************
        """
        xpath_ss_monto_empleador_plazo_indefinido = '//*[@id="p_p_id_56_INSTANCE_88CmNZaRxRaO_"]/div/div/div/table/tbody/tr[4]/td[2]/strong'
        xpath_ss_monto_trabajador_plazo_indefinido = '//*[@id="p_p_id_56_INSTANCE_88CmNZaRxRaO_"]/div/div/div/table/tbody/tr[4]/td[3]/strong'

        xpath_ss_monto_empleador_plazo_fijo = '//*[@id="p_p_id_56_INSTANCE_88CmNZaRxRaO_"]/div/div/div/table/tbody/tr[5]/td[2]/strong'
        xpath_ss_monto_empleador_plazo_indefinido_11anios = '//*[@id="p_p_id_56_INSTANCE_88CmNZaRxRaO_"]/div/div/div/table/tbody/tr[6]/td[2]/strong'
        xpath_ss_monto_empleador_trabajador_casa_particular = '//*[@id="p_p_id_56_INSTANCE_88CmNZaRxRaO_"]/div/div/div/table/tbody/tr[7]/td[2]/strong'

        dict_seguro_sesantia = [
            {
                "contrato": "Plazo indefinido",
                "financiamiento": {
                    "empleador": obtener_valor(xpath_ss_monto_empleador_plazo_indefinido, " ", " "),
                    "trabajador": obtener_valor(xpath_ss_monto_trabajador_plazo_indefinido, " ", " "),
                }
            },{
                "contrato": "Plazo fijo",
                "financiamiento": {
                    "empleador": obtener_valor(xpath_ss_monto_empleador_plazo_fijo, " ", " "),
                    "trabajador": "-",
                }
            },{
                "contrato": "Plazo Indefinido 11 años o más",
                "financiamiento": {
                    "empleador": obtener_valor(xpath_ss_monto_empleador_plazo_indefinido_11anios, " ", " "),
                    "trabajador": "-",
                }
            },{
                "contrato": "Trabajador de Casa Particular",
                "financiamiento": {
                    "empleador": obtener_valor(xpath_ss_monto_empleador_trabajador_casa_particular, " ", " "),
                    "trabajador": "-",
                }
            }
        ]

        list_variables.append({
            "key": 6, 
            "title": "Seguro de cesantía",
            "short_title": "seguro_sesantia",
            "data": dict_seguro_sesantia
        })



        """
        **************************************************
        TASA COTIZACIÓN OBLIGATORIO AFP
        **************************************************
        """

        # Utiliza el XPath para obtener la tabla
        xpath_afp_capital = '//*[@id="p_p_id_56_INSTANCE_wHYq7KvidomO_"]/div/div/div[1]/table'
        tabla = tree.xpath(xpath_afp_capital)

        # Asegúrate de que se haya encontrado la tabla
        if tabla:
            # Selecciona todos los elementos 'tr' dentro de la tabla
            tr_elementos = tabla[0].xpath('.//tr')

            # Inicializa la lista de filas
            filas = []
            list_data_afp = []
            for tr in tr_elementos:
                # Selecciona todos los elementos 'td' dentro de la fila que no tienen la clase 'encabezado_tabla_ind'
                td_elementos = tr.xpath('.//td[not(@class="encabezado_tabla_ind")]')
                fila = [td.text_content().strip() for td in td_elementos]

                # Agrega la fila a la lista de filas
                if fila:
                    filas.append(fila)

            # Imprime las filas
            for fila in filas:
                list_data_afp.append({
                    "afp": fila[0],
                    "trabajador_dependiente": {
                        "tasa_afp": de_string_float_porcentaje(fila[1]),
                        "tasa_sis": de_string_float_porcentaje(fila[2])
                    },
                    "trabajador_independiente": {
                        "tasa_afp": de_string_float_porcentaje(fila[3]),
                    }
                })
            
            list_variables.append({
                "key": 7, 
                "title": "Tasa cotización obligatoria AFP",
                "short_title": "tasa_cotización_obligatoria_afp",
                "data": list_data_afp
            })

                
        else:
            print("No se encontró la tabla con el XPath proporcionado.")


        """
        **************************************************
        ASIGNACION FAMILIAR
        **************************************************
        """
        # Utiliza el XPath para obtener la tabla
        xpath_asignacion_familiar = '//*[@id="p_p_id_56_INSTANCE_BAg5Kc9VLFPt_"]/div/div/div[1]/table'
        tabla = tree.xpath(xpath_asignacion_familiar)

        # Asegúrate de que se haya encontrado la tabla
        if tabla:
            # Selecciona todos los elementos 'tr' dentro de la tabla
            tr_elementos = tabla[0].xpath('.//tr')

            # Inicializa la lista de filas
            filas = []
            list_data_asignacion_familiar = []
            for tr in tr_elementos:
                # Selecciona todos los elementos 'td' dentro de la fila que no tienen la clase 'encabezado_tabla_ind'
                td_elementos = tr.xpath('.//td[not(@class="encabezado_tabla_ind")]')
                fila = [td.text_content().strip() for td in td_elementos]

                # Agrega la fila a la lista de filas
                if fila:
                    filas.append(fila)

            # Imprime las filas
            contador = 1
            for fila in filas:
                tramo = fila[0].split(" ")[1]
                try:
                    monto = int((fila[1].split(" ")[1]).replace(".", ""))
                except:
                    monto = 0

                desde_hasta = fila[2].split(" ")
                
                hasta = int((desde_hasta[len(desde_hasta)-1]).replace(".", ""))
                

                if contador > 1 and contador < len(desde_hasta):
                    desde = int(desde_hasta[3].replace(".", ""))
                else:
                    desde = 0

                list_data_asignacion_familiar.append({
                    "tramo": tramo,
                    "monto": monto,
                    "requisitos": {
                        "desde": desde,
                        "hasta": hasta
                    },
                })
                contador+=1
                

            list_variables.append({
                "key": 8, 
                "title": "asignación familiar",
                "short_title": "asignacion_familiar",
                "data": list_data_asignacion_familiar
            })

        else:
            print("No se encontró la tabla con el XPath proporcionado.")


        """
        **************************************************
        COTIZACIÓN PARA TRABAJOS PESADOS 
        **************************************************
        """
        # Utiliza el XPath para obtener la tabla
        xpath_trabajos_pesados = '//*[@id="p_p_id_56_INSTANCE_z7eabFMiT8St_"]/div/div[1]/div/table'
        tabla = tree.xpath(xpath_trabajos_pesados)

        # Asegúrate de que se haya encontrado la tabla
        if tabla:
            # Selecciona todos los elementos 'tr' dentro de la tabla
            tr_elementos = tabla[0].xpath('.//tr')

            # Inicializa la lista de filas
            filas = []
            list_data_cotizacion_trabajos_pesados = []
            for tr in tr_elementos:
                # Selecciona todos los elementos 'td' dentro de la fila que no tienen la clase 'encabezado_tabla_ind'
                td_elementos = tr.xpath('.//td[not(@class="encabezado_tabla_ind")]')
                fila = [td.text_content().strip() for td in td_elementos]

                # Agrega la fila a la lista de filas
                if fila:
                    filas.append(fila)

            # Imprime las filas
            contador = 1
            for fila in filas:

                porcentaje_puesto_trabajo = int((fila[2].split(" ")[0])[:-1]) + int((fila[3].split(" ")[0])[:-1])
                
                list_data_cotizacion_trabajos_pesados.append({
                    "puesto_trabajo": fila[0],
                    "porcentaje_puesto_trabajo": f"{porcentaje_puesto_trabajo}%",
                    "financiamiento": {
                        "empleador": int((fila[2].split(" ")[0])[:-1]),
                        "trabajador": int((fila[3].split(" ")[0])[:-1])
                    }
                })

            list_variables.append({
                "key": 9, 
                "title": "cotizacion trabajos pesados",
                "short_title": "cotizacion_trabajos_pesados",
                "data": list_data_cotizacion_trabajos_pesados
            })

        else:
            print("No se encontró la tabla con el XPath proporcionado.")


        """
        **************************************************
        DISTRIBUCIÓN DEL 7% SALUD, PARA EMPLEADORES AFILIADO A CCAF (*)
        **************************************************
        """

        # Utiliza el XPath para obtener la tabla
        xpath_trabajos_pesados = '//*[@id="p_p_id_56_INSTANCE_3WYryRoUZVvN_"]/div/div/div/table'
        tabla = tree.xpath(xpath_trabajos_pesados)

        # Asegúrate de que se haya encontrado la tabla
        if tabla:
            xpath_valor_1 = tree.xpath('//*[@id="p_p_id_56_INSTANCE_3WYryRoUZVvN_"]/div/div/div/table/tbody/tr[2]/td[2]/strong/text()')[1]
            xpath_valor_2 = tree.xpath('//*[@id="p_p_id_56_INSTANCE_3WYryRoUZVvN_"]/div/div/div/table/tbody/tr[3]/td[2]/b/text()')[0]

            list_variables.append({
                "key": 10, 
                "title": f"distribucion 7% salud empleadores afiliado ccaf",
                "short_title": "distribucion_salud_empleadores_afiliado_ccaf",
                "data": [
                    {
                        "ccaf": float(((xpath_valor_1.split(" ")[0]).split("%")[0]).replace(",",".")),
                        "fonasa": float(((xpath_valor_2.split(" ")[0]).split("%")[0]).replace(",","."))
                    }
                ]
            })

        else:
            print("No se encontró la tabla con el XPath proporcionado.")


        """
        **************************************************
        Impuesto Único de Segunda Categoría
        **************************************************
        """
        tramo_impuesto_unico_segunda_categoria = [
                {
                    "nombre_tramo": "tramo_1",
                    "porcentaje": 4,
                    "desde": int(13.5 * valor_utm),
                    "hasta": int(30 * valor_utm),
                    "cantidad_rebajar": round(float(0.54 * valor_utm), 2)
                },
                {
                    "nombre_tramo": "tramo_2",
                    "porcentaje": 8,
                    "desde": int(30 * valor_utm),
                    "hasta": int(50 * valor_utm),
                    "cantidad_rebajar": round(float(1.74 * valor_utm), 2)
                },
                {
                    "nombre_tramo": "tramo_3",
                    "porcentaje": 13.5,
                    "desde": int(50 * valor_utm),
                    "hasta": int(70 * valor_utm),
                    "cantidad_rebajar": round(float(4.49 * valor_utm), 2)
                },
                {
                    "nombre_tramo": "tramo_4",
                    "porcentaje": 23,
                    "desde": int(70 * valor_utm),
                    "hasta": int(90 * valor_utm),
                    "cantidad_rebajar": round(float(11.14 * valor_utm), 2)
                },
                {
                    "nombre_tramo": "tramo_5",
                    "porcentaje": 30.4,
                    "desde": int(90 * valor_utm),
                    "hasta": int(120 * valor_utm),
                    "cantidad_rebajar": round(float(17.8 * valor_utm), 2)
                },
                {
                    "nombre_tramo": "tramo_6",
                    "porcentaje": 35,
                    "desde": int(120 * valor_utm),
                    "hasta": int(310 * valor_utm),
                    "cantidad_rebajar": round( float(23.32 * valor_utm), 2)
                },
                {
                    "nombre_tramo": "tramo_7",
                    "porcentaje": 40,
                    "desde": int(310 * valor_utm) ,
                    "hasta": 0,
                    "cantidad_rebajar": round(float(38.82 * valor_utm), 2)
                }
        ]


        list_variables.append({
                "key": 11, 
                "title": f"Impuesto Único de Segunda Categoría",
                "short_title": "impuesto_unico_segunda_categoría",
                "data": tramo_impuesto_unico_segunda_categoria
            })

        return json.dumps(list_variables, ensure_ascii=False)
        
    else:
        print('Error loading page')