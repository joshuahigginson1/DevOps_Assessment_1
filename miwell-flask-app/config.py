# imports ------------------------------

from os import environ, path
from dotenv import load_dotenv

# .env location ------------------------

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


# declare classes ----------------------

class Config(object):
    # General Config

    FLASK_APP = 'wsgi.py'

    # Flask Config from Environment Variables

    SECRET_KEY = environ.get('DEV_SECRET_KEY')
    # FLASK_ENV = environ.get('FLASK_ENV')

    # SQL-Alchemy Database Config

    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Recaptcha Config

    RECAPTCHA_PUBLIC_KEY = environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = environ.get('RECAPTCHA_PRIVATE_KEY')

    # Static Assets Config

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Argon2 Config

    # ARGON2_TIME_COST
    # ARGON2_MEMORY_COST
    # ARGON2_PARALLELISM
    # ARGON2_HASH_LENGTH
    # ARGON2_SALT_LENGTH
    # ARGON2_ENCODING


class ProductionConfig(Config):
    FLASK_ENV = 'production'

    SECRET_KEY = environ.get('PRODUCTION_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('PRODUCTION_DATABASE_URI')


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'

    SECRET_KEY = environ.get('DEV_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')


class TestingConfig(Config):
    TESTING = True
    FLASK_ENV = 'testing'

    SECRET_KEY = environ.get('TEST_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_DATABASE_URI')

    # Selenium Config
    LIVESERVER_PORT = 0  # Set to 0 to have the OS pick the port.
    LIVESERVER_TIMEOUT = 10

