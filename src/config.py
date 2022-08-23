from os import environ

class Config(object):
    TESTING = False
    SECRET_KEY=environ['SECRET_KEY']
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 600

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    pass

class DevelopmentConfig(Config):
    #DATABASE
    DATABASE_USER = environ['DATABASE_USER']
    DATABASE_PASSWORD = environ['DATABASE_PASSWORD']
    DATABASE_ADDRESS = environ['DATABASE_ADDRESS']
    DATABASE_PORT = 3306
    DATABASE_NAME = "flask-blog"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_ADDRESS}:{DATABASE_PORT}/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    #ADMIN
    ADMIN_USER_PASSWORD = environ['ADMIN_USER_PASSWORD']