import json

from django.shortcuts import render
from django.http import HttpResponse
import requests
import operator
import random



def index(request):
    parameters = {'id2': '06_i_orbis.csv'}
    total_empresas = 0
    ingresos_promedio=0
    empleados_promedio=0
    max_paises_abarcados=0
    x='Industria'
    y= 'Total'
    style_data = {'role': 'style'}
    cantidad_empresas_por_sector = [[x, y, style_data]]
    parameters = {'id4': '06_i_orbis.csv'}
    parameters_database = {'id2': '06_i_orbis.csv'}
    empresas_potenciales = []
    empresas_potenciales_param = []
    ingresos_actividad = []
    ingresos_actividad_param = [['Empresas', 'Inversión', style_data]]
    try:
        response_request_data = requests.post('http://127.0.0.1:3000/database_cantidad_empresas_por_sector', data=parameters).json()
        diccionario = response_request_data[0]
        diccionario=dict(sorted(diccionario.items(), key=lambda item: item[1], reverse=True))
        for key in dict(list(diccionario.items())[0:7]):
            cantidad_empresas_por_sector.append([key, diccionario[key], "#3358FF"])
    except:
        cantidad_empresas_por_sector = 'Error'

    try:
        response_request_data = requests.post('http://127.0.0.1:3000/database', data=parameters_database).json()
        total_empresas = response_request_data[0]['1']
        ingresos_promedio = round(response_request_data[1]['1'])
        empleados_promedio = response_request_data[2]['1']
        max_paises_abarcados = response_request_data[3]['1']


        ingresos_actividad = response_request_data[5]['1']

        for actividad in ingresos_actividad[:7]:
            ingresos_actividad_param.append([actividad['Actividad principal'],actividad['Ingresos de explotación (turnover)\nmil USD Últ. año disp.'],"#343957"])

    except:
        ingresos_actividad_param='Error'


    try:
        empresas_potenciales = requests.post('http://127.0.0.1:3000/get_list_companies', data={"id4":10}).json()

        try:
            for empresa in empresas_potenciales:
                empresas_potenciales_param.append(empresa["name"])
            print(empresas_potenciales_param)
            response_request_news = requests.post('http://127.0.0.1:3000/news_scrapper', {"id": empresas_potenciales_param}).json()
        except:
            response_request_news = 'Error'
    except:
        empresas_potenciales = 'Error'

    return render(request, 'inicio.html',
                  {
                      'news_response': response_request_news,
                      'total_empresas': total_empresas,
                      'ingresos_promedio' : ingresos_promedio,
                      'empleados_promedio' : empleados_promedio,
                      'max_paises_abarcados' : max_paises_abarcados,
                      'cantidad_empresas_por_sector' : cantidad_empresas_por_sector,
                      'empresas_potenciales' : empresas_potenciales,
                      'ingresos_actividad_param' : ingresos_actividad_param
                  })

def analisis(request, empresa_param):

    response_request_data = []
    try:
        response_request_data = requests.post('http://127.0.0.1:3000/quest', data={'id1': empresa_param}).json()

    except:
        response_request_data = 'Error'

    cantidad_empleados = response_request_data[0]['cantidad_empleados']
    comparacion_puntajes = response_request_data[0]['comparacion_puntaje']
    style_data = {'role': 'style'}
    comparacion_puntajes_list = [['Empresas', 'Inversión', style_data]]
    pais_destino = response_request_data[0]['pais_destino']
    pais_origen = response_request_data[0]['pais_origen']
    puntaje = response_request_data[0]['puntaje']
    sector = response_request_data[0]['sector']
    for comparacion in comparacion_puntajes:
        #color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
        comparacion_puntajes_list.append([comparacion, float(comparacion_puntajes[comparacion]), "3358FF"])

    try:
        response_request_news = requests.post('http://127.0.0.1:3000/news_scrapper', {"id": empresa_param}).json()
    except:
        response_request_news = 'Error'

    return render(request, 'AnalisisDatos.html',
                  {
                    'nombre': empresa_param,
                    'cantidad_empleados' : cantidad_empleados,
                    'comparacion_puntajes_list' : comparacion_puntajes_list,
                    'pais_destino' : pais_destino,
                    'pais_origen' : pais_origen,
                    'puntaje' : puntaje,
                    'sector': sector,
                    'response_request_news': response_request_news
                  })

def analisis_firts(request):
    empresa = 'error'
    response_request_data = []
    response_empresas = []
    try:
        try:
            response_empresas = requests.post('http://127.0.0.1:3000/get_list_companies', data={"id4": 10}).json()
            empresa = response_empresas[0]['name']
        except:
            empresa='error'
        response_request_data = requests.post('http://127.0.0.1:3000/quest', data={'id1': empresa}).json()
        print(empresa)
    except:
        response_request_data = 'Error'

    cantidad_empleados = response_request_data[0]['cantidad_empleados']
    comparacion_puntajes = response_request_data[0]['comparacion_puntaje']
    style_data = {'role': 'style'}
    comparacion_puntajes_list = [['Empresas', 'Inversión', style_data]]
    pais_destino = response_request_data[0]['pais_destino']
    pais_origen = response_request_data[0]['pais_origen']
    puntaje = response_request_data[0]['puntaje']
    sector = response_request_data[0]['sector']

    for comparacion in comparacion_puntajes:
        #color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
        comparacion_puntajes_list.append([comparacion, float(comparacion_puntajes[comparacion]), "3358FF"])

    try:
        response_request_news = requests.post('http://127.0.0.1:3000/news_scrapper', {"id": empresa}).json()
    except:
        response_request_news = 'Error'

    return render(request, 'AnalisisDatos.html',
                  {
                    'nombre': empresa,
                    'cantidad_empleados' : cantidad_empleados,
                    'comparacion_puntajes_list' : comparacion_puntajes_list,
                    'pais_destino' : pais_destino,
                    'pais_origen' : pais_origen,
                    'puntaje' : puntaje,
                    'sector': sector,
                    'response_request_news': response_request_news
                  })

def bases(request):
    return render(request, 'BasesDatos.html')