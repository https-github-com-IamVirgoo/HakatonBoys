import io
import json
import codecs
import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_data(url: str) -> dict:
    if "?output=" in url and "?output=csv" not in url:
        url = url.split('?output=csv')
        url = f'{url[0]}?output=csv'
    elif '?output=' not in url:
        url = f'{url}?output=csv'
    
    df = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), parse_dates=['Наименование'], index_col=False)
    data = list(df.loc[:, ['Наименование', 'Дата поставки', 'Объем заказа', 'Цена, руб']].T.to_dict().values())
    
    return data


# TODO: override this function
urleur = "https://ru.investing.com/currencies/eur-rub"
url_dollar = "https://ru.investing.com/currencies/usd-rub"
r_usd = requests.get(url_dollar)
r_eur = requests.get(urleur)
usd = BeautifulSoup(r_usd.content, 'html.parser').find('span', class_='text-2xl').text
eur = BeautifulSoup(r_eur.content, 'html.parser').find('span', class_='text-2xl').text 

dollarActual = float(usd.replace(',', '.'))
euroActual = float(eur.replace(',', '.'))
# TODO: override this function





# TODO: override this function
def priceCalc(key):
    # Declaration of variables
    averageDollarPrice = 0
    averageEuroPrise = 0
    counter = 0
    quintity = 0
    dollarStat = [60.9579, 67.0349, 58.3529, 62.7091, 64.7362, 72.1464, 73.6541]
    euroStat = [87.1877, 82.4488, 72.5021, 73.9511, 65.9014, 74.231, 67.7767]
    lastname=''
    
    # Running through the database
    for i in data:
        k = i['Наименование']

        if k!=lastname and lastname == key:
            continue

        if k == key:
            lastname=k
           # print(f'Finded key is {key}')
            counter += 1
            if i['Дата поставки'][:4] == "2015" or i['Дата поставки'][6:10] == "2015":
                averageDollarPrice += float(i['Цена, руб'].replace(',', '.')) / dollarStat[0]
                averageEuroPrise += float(i['Цена, руб'].replace(',', '.')) / euroStat[0]
                quintity += int(i["Объем заказа"])


            if i['Дата поставки'][:4] == "2016" or i['Дата поставки'][6:10] == "2016":
                averageDollarPrice += float(i['Цена, руб'].replace(',', '.')) / dollarStat[1]
                averageEuroPrise += float(i['Цена, руб'].replace(',', '.')) / euroStat[1]
                quintity += int(i["Объем заказа"])


            if i['Дата поставки'][:4] == "2017" or i['Дата поставки'][6:10] == "2017":
                averageDollarPrice += float(i['Цена, руб'].replace(',', '.')) / dollarStat[2]
                averageEuroPrise += float(i['Цена, руб'].replace(',', '.')) / euroStat[2]
                quintity += int(i["Объем заказа"])


            if i['Дата поставки'][:4] == "2018" or i['Дата поставки'][6:10] == "2018":
                averageDollarPrice += float(i['Цена, руб'].replace(',', '.')) / dollarStat[3]
                averageEuroPrise += float(i['Цена, руб'].replace(',', '.')) / euroStat[3]
                quintity += int(i["Объем заказа"])


            if i['Дата поставки'][:4] == "2019" or i['Дата поставки'][6:10] == "2019":
                averageDollarPrice += float(i['Цена, руб'].replace(',', '.')) / dollarStat[4]
                averageEuroPrise += float(i['Цена, руб'].replace(',', '.')) / euroStat[4]
                quintity += int(i["Объем заказа"])


            if i['Дата поставки'][:4] == "2020" or i['Дата поставки'][6:10] == "2020":
                averageDollarPrice += float(i['Цена, руб'].replace(',', '.')) / dollarStat[5]
                averageEuroPrise += float(i['Цена, руб'].replace(',', '.')) / euroStat[5]
                quintity += int(i["Объем заказа"])


            if i['Дата поставки'][:4] == "2021" or i['Дата поставки'][6:10] == "2021":
                averageDollarPrice += float(i['Цена, руб'].replace(',', '.')) / dollarStat[6]
                averageEuroPrise += float(i['Цена, руб'].replace(',', '.')) / euroStat[6]
                quintity += int(i["Объем заказа"])


            if i['Дата поставки'][:4] == "2022" or i['Дата поставки'][6:10] == "2022":
                averageDollarPrice += float(i['Цена, руб'].replace(',', '.')) / dollarActual
                averageEuroPrise += float(i['Цена, руб'].replace(',', '.')) / euroStat
                quintity += int(i["Объем заказа"])


    # Output
    if counter == 0:
        counter += 1
    averageDollarPrice /= counter
    averageEuroPrise/=counter
    quintity /= counter
    averagePriceRUB = (averageDollarPrice*dollarActual + averageEuroPrise*euroActual)/2
    return averagePriceRUB, quintity

top_list = ['Вал 3519.05.02.007','Вал 3519.05.02.083','Вал 3532.10.01.011','Вал 3536.11.01.002','Вал 3572.05.10.150','Вал 3572.05.10.200','ВАЛ-ШЕСТЕРНЯ 3536.11.01.002' ,'Вант стрелы 00.1606.49.1 ','Засов 3532.01.02.007','Зуб  1085.52.05-1','Зуб 1085.52.05-1','Колесо 3519.05.02.003','Колесо 3519.05.02.006','Колесо 3519.05.02.061','Коромысло 3519.21.00.023','Коромысло 3537.25.00.500','Ось 3519.05.02.081','Ось 3519.05.02.082','Ось 3519.21.00.025','Ось 3536.03.00.001','Сателлит 3536.11.01.028']
a=[]
data=json.dump(get_data(url="https://docs.google.com/spreadsheets/d/e/2PACX-1vR5TcnFfw2KNSB0QXgVBmuIpZRad_mcD7XRtVH0zITO1Etzvjfs4Tf2L5aArkOovQ/pub?output=csv"))

for i in top_list:
    a.append(i)
    a.append(priceCalc(i))

if __name__ == "__main__":
    res = get_data(url="https://docs.google.com/spreadsheets/d/e/2PACX-1vR5TcnFfw2KNSB0QXgVBmuIpZRad_mcD7XRtVH0zITO1Etzvjfs4Tf2L5aArkOovQ/pub?output=csv")
    print(res)