from flask import render_template
from flask_restful import Resource

from .views import app
from .views import api
from .getters import price_getter

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
    return render_template('404.html'), 404


class PriceEndpoint(Resource):
    'Gets the price by its name?'
    def get(self, tag):
        return price_getter(tag)


api.add_resource(PriceEndpoint, '/api/v1/price/<string:tag>')