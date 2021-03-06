import data_base
import re
import requests
from bs4 import BeautifulSoup
import random
import json
import time


json_list = data_base.base_1
response_list = data_base.base_2


def find_weather(city, message, bot):
    """Функция поиска погоды"""
    url = 'https://yandex.ru/pogoda/'
    response = requests.get(url + str(city)).text
    soup = BeautifulSoup(response, 'html.parser')
    temp = soup.find('div', {'class': 'content', 'class': 'temp fact__temp'}).find('span',
                                                                                   {'class': 'temp__value'}).text
    str_1 = soup.find('dl', {'class': 'term term_orient_h fact__feels-like'}).find('span',
                                                                                   {'class': 'temp__value'}).text
    str_2 = soup.find('div', {'class': 'fact__condition day-anchor i-bem'}).text
    bot.send_message(message.chat.id,
                     "\t" + str_2 + ". Текущая температура: " + temp + "°" + ". Ощущается как: " + str_1 + "°" +
                     "\n\t(По данным Яндекса)")


def dump(response_dict):
    """Фнкция сброса данных в папка Data"""
    data_base.test_dict_list.append(response_dict)
    if len(data_base.test_dict_list) >= 20:
        with open("Data/%s.json" % str(time.time()), 'wt', encoding='utf8') as file:
            json.dump(data_base.test_dict_list, file, ensure_ascii=False)
        data_base.test_dict_list.clear()


def parsing_string(text, chat_id, context, response_dict):
    """Парсинг текстового файла"""
    for k, v in response_dict.items():
        response_dict[k] = ""
    flag = False
    for dictionary in json_list:
        for key, val in dictionary.items():
            for val_1 in val:
                result = re.search(val_1, text)
                if result is not None:
                    # Если есть значение принадлежащее любому ключу, то проверяем на принадлежность к action
                    temp_dict = data_base.template_dict
                    if key in json_list[1]['action']:
                        response_dict['action'] = key
                        # Создание контекста
                        if context == "" or context != response_dict['action']:
                            temp_dict['context_action'] = key
                            data_base.context_dict[chat_id] = key
                    # ... принадлежность к additional
                    if key in json_list[2]['city']:
                        response_dict['additional'] = 'city'
                        response_dict['city'] = key
                    if key in json_list[0]:
                        response_dict['speech'] = key
    for k, v in response_dict.items():
        if k != 'context_action':
            if response_dict[k] != '':
                flag = True
    if flag == False:
        response_dict['default'] = "1"
    return response_dict


class Bot:
    def __init__(self, message, text, bot):
        self.message = message
        self.text = text
        self.context = data_base.context_dict[message.chat.id] if message.chat.id in data_base.context_dict else ""
        self.bot = bot

    def create_dict(self):
        """Метод парсинга строки"""
        response_dict = data_base.template_dict
        # Находим, есть ли во введенной строке какое-нибудь значение словаря
        response_dict = parsing_string(self.text, self.message.chat.id, self.context, response_dict)
        data_base.test_dict = response_dict
        data_base.dict_list[self.message.chat.id] = response_dict
        dump(response_dict)
        return response_dict

    def pars_dict(self, dct):
        """Метод разбора словаря"""
        bot = self.bot
        message = self.message
        response_dict = dct
        action = response_dict['action']
        additional = response_dict['additional']
        speech = response_dict['speech']
        # Нахождение декорирующих слов
        if speech in json_list[0]:
            bot.send_message(message.chat.id, random.choice(response_list[0][speech]))
        # Есть ли в предложении вопрос о чем то
        if action == 'weather':
            if additional == 'city':
                find_weather(response_dict['city'], self.message, self.bot)
            else:
                bot.send_message(message.chat.id, "Давай уточним город")
        # Ответ по контексту
        elif action == '' and additional == 'city' and data_base.context_dict[message.chat.id] == 'weather':
            find_weather(response_dict['city'], self.message, self.bot)
            data_base.context_dict[message.chat.id] = ""
        elif action == '' and additional == 'city' and data_base.context_dict[message.chat.id] == '':
            bot.send_message(message.chat.id, "Уточни, что ты хочешь")
        # Ответ на непонятное предложение
        elif response_dict['default'] == "1":
            bot.send_message(message.chat.id, random.choice(response_list[1]['pust']))
