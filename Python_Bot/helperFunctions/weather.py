import requests
from decouple import config

API_KEY = config('WEATHER_API')

def get_weather_report(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        temp = str(data['main']['temp'] - 273.15) + ' deg C'
        desc = data['weather'][0]['description']
        feels_like = str(data['main']['feels_like'] - 273.15) + ' deg C'
        pressure = data['main']['pressure']
        humidity = str(data['main']['humidity']) + ' %'
        visibility = str(data['visibility'] / 1000) + ' km'
        max_temp = str(data['main']['temp_max'] - 273.15) + ' deg C'
        min_temp = str(data['main']['temp_min'] - 273.15) + ' deg C'
        wind = str(3.6 * data['wind']['speed']) + ' Km/Hr'

        return {
            "temprature": temp, 
            "weather description": desc,
            "feels_like": feels_like,
            "maximum temperature": max_temp,
            "minimum temperature": min_temp,
            "wind Speed": wind,
            "pressure": pressure,
            "humidity": humidity,
            "visibility": visibility,
            "message": "Have a nice day"
        }
    else:
        return "Error Fetching weather data"