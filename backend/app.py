from flask import Flask
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)