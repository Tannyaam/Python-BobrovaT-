from config import open_weather_token
from pprint import pprint
import requests

def get_weather(city, open_weather_token):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric')
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']

        pprint(f'Погода в городе {city}:\n\nтемпература {cur_weather}C\nвлажность {humidity}%\nдавление {pressure} мм. рт. ст.\nскорость ветра {wind} м/с')

    except Exception as ex:
        pprint('Проверьте название города')
    pass

def main():
    city = input('Введите город: ')
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()
