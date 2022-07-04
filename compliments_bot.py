import requests
import json
import telebot
import telegram
import secrets
import time
from parser import list_of_compliments

bot = telebot.TeleBot("2077649530:AAG-ibfXJxLStNsvwgU85P_AR-5ecGZy51s")

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Привет, Лёль) Я комплимент бот написанный Лякой специально для тебя, если ты запустила этот бот, то значит ты соскучилась по нему, \
        а он работает и не может ответить тебе. Я буду радовать тебя комплиментами при любом твоем сообщении пока Ляка работает на работе мечты)'
  )

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.chat.id, (secrets.choice(list_of_compliments)))
bot.polling()