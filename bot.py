from class_bot import Bot
import json
import data_base
import telebot
from telebot import types
#vndjfkvnkdfnvkdnfvk

bot = telebot.TeleBot(data_base.token)


@bot.message_handler(content_types=['text'])
def text_message(message):
    text = message.text.lower()
    text_obj = Bot(message=message, text=text, bot=bot)
    print(type(message.chat.id))
    print(str(message.chat.id))
    text_obj.create_json()
    text_obj.pars_json()


bot.polling(none_stop=True, interval=0, timeout=0)
