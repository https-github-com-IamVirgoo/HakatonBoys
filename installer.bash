pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_ENV=development
export FLASK_APP=run.py
flask run