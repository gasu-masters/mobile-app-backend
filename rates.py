# Модуль для отправки запросов по HTTP, устанавливается отдельно
import requests
# Модуль для работы с датой и временем, встроенный
import datetime
# Модуль для работы с XML, встроенный
import xml.etree.ElementTree as ET
# Модуль для работы с URL, нужен только если скрипт запускается в компьютерном классе ГАГУ
import urllib.request

# Инструкция по API доступна на https://www.cbr.ru/development/SXML/
BASE_URI = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='
BASE_DATE = '02/03/2002'

# Список основных валют
TARGET_CODES = ['USD', 'EUR']

# Переменная для управления режимом обхода проблемы с прокси:
# - False по умолчанию
# - True если программа запускается в компьютерной сети ГАГУ
GASU_CLASSROOM = False

# Функция нужна для обхода проблемы с прокси в компьютерном классе ГАГУ
def api_get(url = ''):
    """
    Отправить GET-запрос на указанный URL

    url -- URL, который требуется запросить
    """
    # Дополнительные манипуляции для обхода проблемы с прокси
    if (GASU_CLASSROOM):
        proxies = urllib.request.getproxies()
        url = url.replace('https://', 'http://')
        response = requests.get(url, proxies)
    else:
        response = requests.get(url)

    return response

def today_date_formatted():
    """
    Вернуть сегодняшнюю дату в формате, который ожидает API ЦБ РФ
    """
    return datetime.date.today().strftime('%d/%m/%Y')

def rates_for_date(date = BASE_DATE):
    """
    Запросить курсы валют на заданную дату
    
    date -- дата, для которой делать запрос (по умолчанию BASE_DATE)
    """
    response = api_get(BASE_URI + date)

    # Парсим: преобразуем данные от API в структуры данных Python (списки, словари)
    root = ET.fromstring(response.content)
    result = []
    
    for child in root:
        element = {
            'ID': child.attrib['ID'],
        }
        for subchild in child:
            element[subchild.tag] = subchild.text
        
        result.append(element)

    return result

def target_rates_for_today():
    """
    Получить курсы валют на сегодняшнюю дату
    """
    today = today_date_formatted()
    rates = rates_for_date(today)

    # Фильтруем список, полученный от API, выбираем только нужные валюты
    return [x for x in rates if x['CharCode'] in TARGET_CODES]
