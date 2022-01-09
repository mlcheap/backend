import os
FLASK_APP = "app.py"
APP_SETTINGS = "development"
MONGO_URI= os.getenv('MONGO_URL') or "mongodb://localhost:27017"
MONGO_DBNAME = 'labeler'

SECRET_KEY = 'mysql://root:CE2YpiFA@g@localhost:'
REDIS_HOST = u'localhost'
REDIS_PORT = 6379

