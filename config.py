import os
from dotenv import load_dotenv


# load environmental variables
load_dotenv()

# Database configuration
DB_CONFIG = {
    'server': os.environ.get('DB_SERVER'),
    'database': os.environ.get('DB_NAME'),
    'username': os.environ.get('DB_USERNAME'),
    'password': os.environ.get('DB_PASSWORD'),
}

# Secret key for sessions and CSRF protection
SECRET_KEY = os.environ.get('SECRET_KEY', os.environ.get('SECRET_KEY'))

# Debug mode
DEBUG = True

# Application root URL
APPLICATION_ROOT = '/'

# Config settings
class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mssql+pymssql://sa:Kheriac@1@localhost/imageDB"
