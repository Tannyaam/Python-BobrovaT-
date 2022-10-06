import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет! Напиши название города и я пришлю сводку погоды!')


@dp.message_handler()
async def get_weater(message: types.Message):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']

        await message.reply(f'Погода в городе {city}:\n\nтемпература {cur_weather}C\nвлажность {humidity}%\nдавление {pressure} мм. рт. ст.\nскорость ветра {wind} м/с')

    except Exception as ex:
        await message.reply('Проверьте название города')
    pass


if __name__ == '__main__':
    executor.start_polling(dp)