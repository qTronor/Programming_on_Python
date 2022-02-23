import os

import telebot
import time

bot = telebot.TeleBot('904686090:AAHERKVeFae3lc_BMf9SqFmTVxnIJRHy_k0')
@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Привет, Я твой персональный ассистент Пётр')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/' + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)

bot.polling()