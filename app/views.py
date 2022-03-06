from flask import Flask
from flask import render_template
from flask_restful import Api, Resource

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

class Price(Resource):
    def get(self, price):
        print(f"Getted price: {price}" )
        return {'content': 'none'}


api.add_resource(Price, '/api/v1/<string:price>')