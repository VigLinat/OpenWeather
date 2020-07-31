import requests
import json

def get_current_weather(city, APIkey):
    current_weather_path = 'https://api.openweathermap.org/data/2.5/weather'
    APIparams = {'q' : city, 'APPID' : APIkey}
    request_handler = requests.get(current_weather_path, params = APIparams)

    return request_handler
                                   

APIkey = 'ee3c9674a0567d97347a5b1a34e8171f'
city = 'Sevastopol'

if (__name__ == '__main__'):
    
    r = get_current_weather(city, APIkey) 

    try:
        data = r.json()
        print(data)
        print('\n')
    except ValueError as e:
        print(e)

    
