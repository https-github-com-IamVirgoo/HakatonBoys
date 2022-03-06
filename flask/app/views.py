from flask import render_template
from app import app

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
