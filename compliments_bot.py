import requests
import json
import telebot
import telegram
import secrets
import time
from parser import list_of_compliments

#add your bot token below
bot = telebot.TeleBot("x.x.x.x")

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id, 'Hi, it\'s a bot to write you a compliments for every your message, enjoy')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.chat.id, (secrets.choice(list_of_compliments)))
bot.polling()
