import telebot
import requests
import json

api_token = '5750716847:AAH3xvr2fTvIUUgIXhizLtmjTv0JX_WHIls'

url = "https://api.weather.yandex.ru/v2/informers?lat=55.75222&lon=37.61556"
headers = {"X-Yandex-API-Key": "fd038f59-339f-4cf9-9d98-ab8a60ec9586"}

bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def get_weather(message):
    bot.send_message(message.chat.id, text=f'Привет, {message.from_user.username}!\n\nРасскажу о погоде по команде /get_weather')

@bot.message_handler(commands=['get_weather'])
def get_weather(message):
    r = requests.get(url=url, headers=headers)
    bot.send_message(message.chat.id, r.text)
    if r.status_code == 200:
        data = json.loads(r.text)
        fact = data["fact"]
        bot.send_message(message.chat.id, text=f'Now {fact["temp"]}°, feels like {fact["feels_like"]}°. Now on the street {fact["condition"]}')
    else:
        bot.send_message(message.chat.id, 'Problems on weather API')

bot.polling(none_stop=True)