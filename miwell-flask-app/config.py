# imports ------------------------------

from os import environ, path
from dotenv import load_dotenv

# .env location ------------------------

basedir = path.abspath(path.dirname(__file__))  # We find the absolute path of the root directory of our current file.
load_dotenv(path.join(basedir, '.env'))  # Load our specific .env file from the root directory of our current file.


# declare classes ----------------------

class Config(object):  # General Config

    FLASK_APP = 'wsgi.py'

    DEBUG = False
    TESTING = False

    # Database and SQL Alchemy Config

    DB_NAME = 'miwell_production_database.'
    SQLALCHEMY_DATABASE_URI = environ.get('PRODUCTION_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security Config

    SESSION_COOKIE_SECURE = True

    SECRET_KEY = environ.get('PRODUCTION_SECRET_KEY')

    # ARGON2_TIME_COST
    # ARGON2_MEMORY_COST
    # ARGON2_PARALLELISM
    # ARGON2_HASH_LENGTH
    # ARGON2_SALT_LENGTH
    # ARGON2_ENCODING

    # Recaptcha Config

    # RECAPTCHA_PUBLIC_KEY = environ.get('RECAPTCHA_PUBLIC_KEY')
    # RECAPTCHA_PRIVATE_KEY = environ.get('RECAPTCHA_PRIVATE_KEY')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):

    DEBUG = True

    # Database and SQL Alchemy Config

    DB_NAME = 'miwell_dev_database'
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security Config

    SESSION_COOKIE_SECURE = False

    SECRET_KEY = environ.get('DEV_SECRET_KEY')


class TestingConfig(Config):

    TESTING = True

    # Database and SQL Alchemy Config

    DB_NAME = 'miwell_test_database'
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security Config

    SESSION_COOKIE_SECURE = False

    SECRET_KEY = environ.get('TEST_SECRET_KEY')

    # Selenium Config

    LIVESERVER_PORT = 8943  # Set to 0 to have the OS pick the port.
    LIVESERVER_TIMEOUT = 10


# It is good practice to specify configurations for different environments.
# Below, we consolidate these configuration names into a dictionary.

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

