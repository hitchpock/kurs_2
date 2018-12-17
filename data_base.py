import re
import json
base_1 = [
    {
        "set_hello": [r"привет\w*", r"хай\w*", r"здорова\w*"],
        "set_vopr": [r"как дела?\w*", r"что делаешь?\w*"],
        "set_nastr_bad": [r"плохо\w*", r"отстой\w*"],
        "set_nastr_good": [r"круто\w*", r"классно\w*", r"зашибись\w*"],
    },
    {
        "action": ["weather"],
        "additional": ["city"]
    },
    {
        "city": ["Moscow", "Saint-Petersburg"]
    },
    {
        "Moscow": [r"москв\w*", "мск"],
        "Saint-Petersburg": [r"петербург\w*", r"питер\w*"]
    },
    {
        "weather": [r"погод\w*"]
    }
]

base_2 = [
    {
        # Фразы для ответа
        'set_hello': ['Привет', 'Ку', 'Хай', 'Здорова'],
        'set_vopr': ['У меня все хорошо. Сижу развлекаюсь =)'],
        'set_nastr_bad': ['Это не радует('],
        'set_nastr_good': ['Это прекрасно!']
    },
    {
        # Пустые фразы
        'pust': ['Хм... надо подумать', 'Спроси немного точнее', 'Скорее всего, я пока не знаю таких команд'],
    }
]

template_dict = {
    "action": "",
    "additional": "",
    "context_action": "",
    "speech": "",
    "default": ""
}

test_dict = {
    "action": "",
    "additional": "",
    "context_action": "",
    "speech": "",
    "default": ""
}

dict_list = {}

test_dict_list = []

context_dict = {}

token = '581160657:AAF4_D69PkS3-0yoS9Exw7pEE3-anFx8FNs'

with open('city.json', 'rt', encoding='utf8') as file:
    city_json = json.load(file)

city_dict = dict(city_json)
for i in city_dict:
    if len(i) <= 4:
        del city_dict[i]

base_1.append(city_dict)
base_1[2]['city'] += base_1[5].keys()
