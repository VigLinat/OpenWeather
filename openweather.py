import requests
import openweathermapapi as api

from datetime import datetime
#conversion from unix timestamp to readable date-time:
#print(datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S'))

def main():
    APIkey = 'ee3c9674a0567d97347a5b1a34e8171f'
    city = 'Sevastopol'

    #r = api.get_current_weather(city, APIkey)
    r = api.get_forecast(city, APIkey)
    print('message cod: ', r.json()['cod'])

    with open('log.txt', 'w') as log:
        log.write(r.text)

    data = r.json()

    api.print_formatted_weather(data)

if (__name__ == '__main__'):
    main()
