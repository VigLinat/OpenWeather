import requests
messages = {200 : 'OK', 401 : 'invalid API key'}

def get_error_message(code_message):
    return messages[code_message]

def get_current_weather(city, APIkey):
    #api request for current weather
    api_addres = 'https://api.openweathermap.org/data/2.5/weather'
    APIparams = {'q' : city, 'APPID' : APIkey}
    request_handler = requests.get(api_addres, params = APIparams)
    return request_handler

def get_forecast(city, APIkey):
    #api request for 5 day / 3 hour forecast
    api_addres = 'https://api.openweathermap.org/data/2.5/forecast'
    APIparams = {'q' : city, 'APPID' : APIkey}
    request_handler = requests.get(api_addres, params = APIparams)
    #forecast returns list of dictionaries
    #weather['list'][1]['main']['temp'] example
    return request_handler

def print_formatted_weather(weather):
    #weather is dictionary about weather data
    #prints formatted output for 5 day forecast or current weather
    if 'list' in weather:
        #if there is a "list" param, weather is a forecast,
        #else, weather is a current weather
        counter = weather['cnt']
        weather = weather['list']
    else:
        counter = -1

    if counter >= 0:
        i = 0
        prev_day = weather[0]['dt_txt'][8:10] #positions 8,9 contains month's day
        while i < counter:
            cur_day = weather[i]['dt_txt'][8:10]
            if (cur_day != prev_day):
                print('date: ', weather[i]['dt_txt'][0:11])
            print('UTC time: ',weather[i]['dt_txt'][11:19], '\ntemperature: ', weather[i]['main']['temp'] - 273.15)
            print('clouds: ', weather[i]['weather'][0]['main'],\
                ' ', weather[i]['clouds']['all'])
            prev_day = cur_day
            i = i + 1
            print('\n')
    else:
        print('date & time: ', weather['dt_txt'])
        print('temperature: ', weather['main']['temp'] - 273.15)
        print('clouds: ', weather['weather']['main'],
            ' ', weather['clouds']['all'])
