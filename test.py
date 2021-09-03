from itertools import islice

import requests
import random

try:
    response_request_data = requests.post('http://127.0.0.1:3000/quest', data={'id1': 'Royal profit'}).json()

except:
    response_request_data = 'Error'

cantidad_empleados = response_request_data[0]['cantidad_empleados']
comparacion_puntajes = response_request_data[0]['comparacion_puntaje']
style_data = {'role': 'style'}
comparacion_puntajes_list = [['Empresas', 'Inversión', style_data]]
pais_destino = response_request_data[0]['pais_destino']
pais_origen = response_request_data[0]['pais_origen']
puntaje = response_request_data[0]['puntaje']

for comparacion in comparacion_puntajes:
    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    comparacion_puntajes_list.append([comparacion, float(comparacion_puntajes[comparacion]), "".join(color)])
try:
    response_request_news = requests.post('http://127.0.0.1:3000/news_scrapper', {"id": ['royal profit']}).json()
except:
    response_request_news = 'Error'

print(response_request_news)