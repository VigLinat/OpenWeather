import requests

def get_current_weather(city, APIkey):
    current_weather_path = 'https://api.openweathermap.org/data/2.5/weather'
    APIparams = {'q' : city, 'APPID' : APIkey}
    request_handler = requests.get(current_weather_path, params = APIparams)
    return request_handler

def get_5_day_forecast(city, APIkey):
    current_weather_path = 'api.openweathermap.org/data/2.5/forecast'
    APIparams = {'q' : city, 'APPID' : APIkey}
