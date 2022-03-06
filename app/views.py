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


api.add_resource(Price, '/api/v1/<string:price>')

#--------------------------------------------------------------------------------------------------------------------------------------------------

def DollarParse():
    url = "https://ru.investing.com/currencies/usd-rub"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    usd = soup.find('span', class_='text-2xl').text
    return usd

with open('db.json', 'r') as databasefile:
    data = json.load(databasefile)

def get_by_key(key: str):
    return data[key]