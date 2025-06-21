import os

class Config:
   MAIL_USERNAME = '<your-gmail-username>@gmail.com'
   MAIL_PASSWORD = 'htue qczu rnxo codx'
   MAIL_DEFAULT_SENDER = '<your-gmail-username>@gmail.com'
   MONGO_URI = '<mongodb connection string>'
   DATABASE_NAME = 'newsletter'
   ALLOWED_IPS = ['127.0.0.1']
   MAIL_SERVER = 'smtp.gmail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'
   RESULT_BACKEND = MONGO_URI + '/celery_results'




