import io
import json
import codecs
import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR5TcnFfw2KNSB0QXgVBmuIpZRad_mcD7XRtVH0zITO1Etzvjfs4Tf2L5aArkOovQ/pub?output=csv"


df = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), parse_dates=['Наименование'], index_col=False)
data = json.loads(json.dumps(list(df.loc[:, ['Наименование', 'Дата поставки', 'Объем заказа', 'Цена, руб']].T.to_dict().values())))


# TODO: override this function
def DollarParse() -> str:
    url = "https://ru.investing.com/currencies/usd-rub"
    r = re.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    usd = soup.find('span', class_='text-2xl').text
    return usd

# TODO: override this function
def EuroParse() -> str:
    url = "https://ru.investing.com/currencies/eur-rub"
    r = re.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    eur = soup.find('span', class_='text-2xl').text
    return eur    

# TODO: override this function
def priceCalc(key):
    # Declaration of variables
    averageDollarPrice = 0
    averageEuroPrise = 0
    counter = 0
    quintity = 0
    dollarStat = [60.9579, 67.0349, 58.3529, 62.7091, 64.7362, 72.1464, 73.6541]
    euroStat = [87.1877, 82.4488, 72.5021, 73.9511, 65.9014, 74.231, 67.7767]

    dollarActual = float(DollarParse().replace(',', '.'))
    euroActual = float(EuroParse().replace(',', '.'))

    # Running through the database

    for i in data:
        k = i['Наименование']
        if k == key:
            print(f'Finded key is {key}')
            counter += 1
            if i['ДатаПоставки'][:4] == "2015" or i['ДатаПоставки'][6:10] == "2015":
                averageDollarPrice += float(i['Цена'].replace(',', '.')) / dollarStat[0]
                averageEuroPrise += float(i['Цена'].replace(',', '.')) / euroStat[0]
                quintity += int(i["ОбъемЗаказа"])


            if i['ДатаПоставки'][:4] == "2016" or i['ДатаПоставки'][6:10] == "2016":
                averageDollarPrice += float(i['Цена'].replace(',', '.')) / dollarStat[1]
                averageEuroPrise += float(i['Цена'].replace(',', '.')) / euroStat[1]
                quintity += int(i["ОбъемЗаказа"])

            if i['ДатаПоставки'][:4] == "2017" or i['ДатаПоставки'][6:10] == "2017":
                averageDollarPrice += float(i['Цена'].replace(',', '.')) / dollarStat[2]
                averageEuroPrise += float(i['Цена'].replace(',', '.')) / euroStat[2]
                quintity += int(i["ОбъемЗаказа"])

            if i['ДатаПоставки'][:4] == "2018" or i['ДатаПоставки'][6:10] == "2018":
                averageDollarPrice += float(i['Цена'].replace(',', '.')) / dollarStat[3]
                averageEuroPrise += float(i['Цена'].replace(',', '.')) / euroStat[3]
                quintity += int(i["ОбъемЗаказа"])

            if i['ДатаПоставки'][:4] == "2019" or i['ДатаПоставки'][6:10] == "2019":
                averageDollarPrice += float(i['Цена'].replace(',', '.')) / dollarStat[4]
                averageEuroPrise += float(i['Цена'].replace(',', '.')) / euroStat[4]
                quintity += int(i["ОбъемЗаказа"])

            if i['ДатаПоставки'][:4] == "2020" or i['ДатаПоставки'][6:10] == "2020":
                averageDollarPrice += float(i['Цена'].replace(',', '.')) / dollarStat[5]
                averageEuroPrise += float(i['Цена'].replace(',', '.')) / euroStat[5]
                quintity += int(i["ОбъемЗаказа"])

            if i['ДатаПоставки'][:4] == "2021" or i['ДатаПоставки'][6:10] == "2021":
                averageDollarPrice += float(i['Цена'].replace(',', '.')) / dollarStat[6]
                averageEuroPrise += float(i['Цена'].replace(',', '.')) / euroStat[6]
                quintity += int(i["ОбъемЗаказа"])

            if i['ДатаПоставки'][:4] == "2022" or i['ДатаПоставки'][6:10] == "2022":
                averageDollarPrice += float(i['Цена'].replace(',', '.')) / dollarActual
                averageEuroPrise += float(i['Цена'].replace(',', '.')) / euroStat
                quintity += int(i["ОбъемЗаказа"])

    # Output
    if counter == 0:
        counter += 1
    averageDollarPrice /= counter
    averageEuroPrise/=counter
    quintity /= counter
    averagePrice = (averageDollarPrice*dollarActual + averageEuroPrise*euroActual)/2
    return averagePrice, quintity