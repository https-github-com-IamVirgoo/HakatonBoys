import json

from flask import Flask
from flask import render_template
from flask_restful import Api, Resource
import psycopg2
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
api = Api(app)


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/')
@app.route('/index')
def index():
    return  render_template("index.html")


@app.route('/doc')
def doc():
    return  render_template("doc.html")


@app.route('/work')
def work():
    return  render_template("work.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
class Price(Resource):
    def get(self, price):
        print(f"Getted price: {price}" )
        return {'content': "ababa"}


class Prices(Resource):
    def get(self, key):
        print(f"Getting {key}")
        return {'content': priceCalc(key)}

api.add_resource(Price, '/api/v1/<string:price>')
api.add_resource(Prices, '/api/v2/<string:key>')

#--------------------------------------------------------------------------------------------------------------------------------------------------

def priceCalc(key):

    # Create the dollar parser

    def DollarParse():
        url = "https://ru.investing.com/currencies/usd-rub"
        headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_23 like Mac OS X) '
                                 'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        usd = soup.find('span', class_='text-2xl').text
        return usd

    # Open the json file with data

    with codecs.open('message.json', 'r', 'utf-8') as databasefile:
        data = json.load(databasefile)['cont']

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

    averagePrice /= counter
    return averagePrice