from flask import Flask
from flask_mail import Mail
from flask_pymongo import PyMongo
from celery import Celery

# Create a Flask application
app = Flask(__name__)
app.config.from_object('config.Config')

# Create a Flask-Mail instance
mail = Mail(app)

# Connect to MongoDB
client = PyMongo(app).cx
db = client[app.config['DATABASE_NAME']]

# Create a Celery instance
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from routes import *
from tasks import *

if __name__ == '__main__':
   app.run(debug=True)
