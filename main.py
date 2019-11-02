import pyowm
owm = pyowm.OWM("85b7235ca94da8d941ddfc41f9cd7e51")
observation = owm.weather_at_place("North Sydney, AU")

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

print(getWeather()['humi'])
#test