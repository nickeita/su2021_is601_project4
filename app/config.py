from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.app(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    DEBUG = True

    LESS_BIN = '/venv/bin/lessc'
    ASSETS_DEBUG = False
    ASSETS_AUTO_BUILD = True

    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
