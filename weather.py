import requests
import pycountry
import math
import json

from requests.api import get

city_name = 'Barcelona'
api_key = '0377a5b8be0340cb6bc8123a7dd02834'
# url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
# response = requests.get(url).json()
# print(response)


'''
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url).json()

   temp = response['main']['temp']
    temp = math.floor((temp * 1.8) - 459.67)  # Convert to °F
    print(temp)

    feels_like = response['main']['feels_like']
    feels_like = math.floor((feels_like * 1.8) - 459.67)  # Convert to °F

    humidity = response['main']['humidity']

    main =  response['weather']['description']
    
    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity,
        'main': main
    }
'''

def basic(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    json_resp = json.loads(response.text)
    weather = json_resp['weather']
    main = weather[0]
    main_field = main['main']
    return(main_field) # Will be "Clouds"

def country(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    countryShort = response['sys']['country']
    countryInfo = pycountry.countries.get(alpha_2=countryShort)
    countryName = countryInfo.name
    return(countryName)

def temperature(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    print(response)
    temp = response['main']['temp']
    temp = math.floor((temp * 1.8) - 459.67)  # Convert to °F
    return(temp)

def temp_max(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    temp_max = response['main']['temp_max']
    temp_max = math.floor((temp_max * 1.8) - 459.67)  # Convert to °F
    return(temp_max)

def temp_min(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    temp_min = response['main']['temp_min']
    temp_min = math.floor((temp_min * 1.8) - 459.67)  # Convert to °F
    return(temp_min)

def feels_like(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    feels_like = response['main']['feels_like']
    feels_like = math.floor((feels_like * 1.8) - 459.67)  # Convert to °F
    return(feels_like)