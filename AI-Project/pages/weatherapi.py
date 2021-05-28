# Author: Tiago Silva
# Version: 1.1
import requests


def getWeather(city):
    url = "https://www.metaweather.com/api/location/search/?query=" + city
    resp1 = requests.get(url).json()
    cityCode = resp1[0]['woeid']
    url2 = "https://www.metaweather.com/api/location/" + str(cityCode)
    resp1 = requests.get(url2).json()
    today = resp1['consolidated_weather'][0]
    state = today['weather_state_name']
    minTemp = str(today['min_temp'])[0:2]
    maxTemp = str(today['max_temp'])[0:2]
    return [state, minTemp, maxTemp]


