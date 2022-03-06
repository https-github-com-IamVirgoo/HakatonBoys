import json
import codecs

import requests as re

# Data base 
with codecs.open('app/message.json', 'r', 'utf-8') as databasefile:
    data = json.load(databasefile)['cont']


def price_getter(tag: str) -> dict:
    'Returns dict with data'
    ...


def DollarParse() -> str:
    url = "https://ru.investing.com/currencies/usd-rub"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    usd = soup.find('span', class_='text-2xl').text
    return usd


def priceCalc(key):

    # Declaration of variables
    averagePrice = 0
    counter = 0
    dollarStat = [60.9579, 67.0349, 58.3529, 62.7091, 64.7362, 72.1464, 73.6541]
    dollarActual = float(DollarParse().replace(',', '.'))

    # Running through the database

    for i in data:
        k = i['Наименование']
        if k == key:
            counter += 1
            if i['ДатаПоставки'][:4] == "2015" or i['ДатаПоставки'][6:10] == "2015":
                averagePrice += float(i['Цена'].replace(',', '.')) / dollarStat[0]

            if i['ДатаПоставки'][:4] == "2016" or i['ДатаПоставки'][6:10] == "2016":
                averagePrice += float(i['Цена'].replace(',', '.')) / dollarStat[1]

            if i['ДатаПоставки'][:4] == "2017" or i['ДатаПоставки'][6:10] == "2017":
                averagePrice += float(i['Цена'].replace(',', '.')) / dollarStat[2]

            if i['ДатаПоставки'][:4] == "2018" or i['ДатаПоставки'][6:10] == "2018":
                averagePrice += float(i['Цена'].replace(',', '.')) / dollarStat[3]

            if i['ДатаПоставки'][:4] == "2019" or i['ДатаПоставки'][6:10] == "2019":
                averagePrice += float(i['Цена'].replace(',', '.')) / dollarStat[4]

            if i['ДатаПоставки'][:4] == "2020" or i['ДатаПоставки'][6:10] == "2020":
                averagePrice += float(i['Цена'].replace(',', '.')) / dollarStat[5]

            if i['ДатаПоставки'][:4] == "2021" or i['ДатаПоставки'][6:10] == "2021":
                averagePrice += float(i['Цена'].replace(',', '.')) / dollarStat[6]

            if i['ДатаПоставки'][:4] == "2022" or i['ДатаПоставки'][6:10] == "2022":
                averagePrice += float(i['Цена'].replace(',', '.')) / dollarActual

    # Output
    if counter == 0:
        counter += 1
    averagePrice /= counter
    return averagePrice