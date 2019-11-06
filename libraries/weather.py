# Reads weather data from Open Weather Map and calculates if
# the weather is good enough for astrophotography.

import pyowm
import configparser 

config = configparser.ConfigParser()
config.read('config.ini')

owm = pyowm.OWM("85b7235ca94da8d941ddfc41f9cd7e51")

latitude = float(config.get('location', 'lat'))
longitude = float(config.get('location', 'long'))
observation = owm.weather_at_coords(latitude, longitude)

threashold = 85

def getWeather():
    weather = observation.get_weather()
    temperature = weather.get_temperature('celsius')['temp']
    humidity = weather.get_humidity()
    cloudCover = weather.get_clouds() 
    rain = weather.get_rain()
    wind = weather.get_wind()['speed']
    sunrise = weather.get_sunrise_time(timeformat='iso')
    sunset = weather.get_sunset_time(timeformat='iso')
    CurrentWeatherDict = { 
        "temp": temperature,
        "wind": wind,
        "rain": rain,
        "humi": humidity,
        "covr": cloudCover,
        "sset": sunset,
        "sris": sunrise
    }
    return CurrentWeatherDict

def getForcast():
    fc = owm.three_hours_forecast('North Sydney, AU')
    f = fc.get_forecast()
    lst = f.get_weathers()
    for weather in f:
        print (weather.get_reference_time('iso'),weather.get_clouds())

def weatherStatus(threash = threashold):
    weather = getWeather()
    covr = weather['covr']
    humi = weather['humi']
    wind = weather['wind']
    try:
        rain = int(weather['rain'])
    except:
        rain = 0
    weatherScore = (int(covr) + int(humi)) * (int(rain) + 1) + wind
    if weatherScore < threash:
        return True
    else:
        return False, weatherScore