#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
from decouple import config

default_city = 'milan'
geolocation_api = 'https://ipapi.co/json'

temperature = ''
recognized_city = ''

try:
    api_key = config('OPENWEATHER_API_KEY')
    location_response = requests.get(geolocation_api)
    location_data = json.loads(location_response.text)
    current_city = location_data["city"]

    weather_api = "https://api.openweathermap.org/data/2.5/weather?q=%s&lang=it&appid=%s" % (default_city if not current_city else current_city, api_key)

    weather_response = requests.get(weather_api)
    weather_data = json.loads(weather_response.text)
    temperature = weather_data["main"]["temp"] - 273.15 # Conversion from Kelvin to Celsius
    recognized_city = weather_data["name"]
except:
    temperature = ''
    recognized_city = ''
finally:
    print("Temperature in %s is %i C" % (recognized_city, temperature) if recognized_city and temperature else 'Error: not possible to get data')