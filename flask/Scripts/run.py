#!flask/bin/python
from app import app

app.static_folder = 'static'

app.run(debug = True)
