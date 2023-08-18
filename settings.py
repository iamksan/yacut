import os
from string import ascii_letters, digits

ALLOWED_CHARACTERS = ascii_letters + digits
CUSTOM_ID_PATTERN = r'^[A-Za-z0-9]+$'
STATIC_DIR = os.path.abspath('./html')
TEMPLATE_DIR = os.path.join(STATIC_DIR, 'templates')

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'MY_SECRET_KEY') 