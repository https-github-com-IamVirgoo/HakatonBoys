import json
import codecs

from flask import Flask
from flask_restful import Api
import psycopg2
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
api = Api(app)