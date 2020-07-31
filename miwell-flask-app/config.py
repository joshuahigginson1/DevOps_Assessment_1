# imports ------------------------------

from os import environ, path
from dotenv import load_dotenv

# .env location ------------------------

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


# declare classes ----------------------

class Config(object):
    # General Config

    DEBUG = False
    TESTING = False
    FLASK_APP = 'wsgi.py'

    # Flask Config from Environment Variables

    # SECRET_KEY = environ.get('SECRET_KEY')
    # FLASK_ENV = environ.get('FLASK_ENV')

    # SQL-Alchemy Database Config

    # SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    # SQLALCHEMY_ECHO = False
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Static Assets Config

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
