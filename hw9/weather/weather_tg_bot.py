import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

button1 = KeyboardButton('Tokyo')
button2 = KeyboardButton('Madrid')
button3 = KeyboardButton('Oslo')
button4 = KeyboardButton('New York')
button5 = KeyboardButton('Sydney')
button6 = KeyboardButton('Mumbai')

markup3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).add(button3).add(button4).add(button5).add(button6)

@dp.message_handler(commands=['more_cities'])
async def process_hi3_command(message: types.Message):
    await message.reply("Узнай погоду в других городах", reply_markup=markup3)

@dp.message_handler(commands=['start'])
async def get_weather_command(message: types.Message):
    await message.reply('Привет! Напиши название города и я пришлю сводку погоды!')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('Доступные команды:\n/start - запуск бота\n/more_cities - информация о погоде в городах из списка\n/help - все команды')

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