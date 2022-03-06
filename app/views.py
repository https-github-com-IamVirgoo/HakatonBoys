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
        return {'content': Price_Calculation(price)}


class Prices(Resource):
    def get(self, key):
        print(f"Getting {key}")
        return {'content': get_by_key(key)}

api.add_resource(Price, '/api/v1/<string:price>')
api.add_resource(Prices, '/api/v2/<string:key>')

#--------------------------------------------------------------------------------------------------------------------------------------------------

def DollarParse():
    url = "https://ru.investing.com/currencies/usd-rub"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    usd = soup.find('span', class_='text-2xl').text
    return usd

with open('app/message.json', 'r') as databasefile:
    data = json.load(databasefile)['cont']

def get_by_key(key: str):
    for i in data:
        print(i['Наименование'])
        k = i['Наименование'].split(' ')[2]
        print(k)
        if k == key:
            return {
                'Name': i['Наименование'],
                'DelivDate': i['ДатаПоставки'],
                'Price': i['Цена'],
                'Amount': i['ОбъемЗаказа']
            }