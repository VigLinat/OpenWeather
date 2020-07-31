import requests
import openweathermapapi as api

from datetime import datetime
#conversion from unix timestamp to readable date-time:
#print(datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S'))

APIkey = 'ee3c9674a0567d97347a5b1a34e8171f'
city = 'Sevastopol'

weather = ['weather', 'main', 'wind', 'clouds']

r = api.get_current_weather(city, APIkey)

with open('log.txt', 'w') as log:
    log.write(r.text)

data = r.json()

print('current GMT+3 time : ', datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S'))
for param in weather:
     if param in data:
         print(param, ' : ', data[param])
