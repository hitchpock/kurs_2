from class_bot import Bot
import data_base
import telebot

bot = telebot.TeleBot(data_base.token)


@bot.message_handler(content_types=['text'])
def text_message(message):
    text = message.text.lower()
    text_obj = Bot(message=message, text=text, bot=bot)
    dct = text_obj.create_dict()
    text_obj.pars_dict(dct)


bot.polling(none_stop=True, interval=0, timeout=0)
