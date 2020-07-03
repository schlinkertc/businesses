"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname('black_owned_businesses'))
load_dotenv(path.join(BASE_DIR, '.env'))

class Config:
    """Flask configuration variables."""
    
    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = 'wsgi.py'
    FLASK_ENV = 'development'
    TESTING = True
    FLASK_DEBUG = 1

    # Assets
    LESS_BIN = path.join(BASE_DIR,'node_modules/.bin/lessc')
    ASSETS_DEBUG = True
    ASSETS_AUTO_BUILD = True

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')
    
    #SQLAlchemy
    database_name = 'black_owned_businesses'
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')+database_name+'?charset=UTF8MB4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #Yelp and Mapbox
    yelp_api_key = environ.get('YELP_API_KEY')
    mapbox_access_token = environ.get('MAPBOX_ACCESS_TOKEN')