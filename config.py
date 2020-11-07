import os

class Config:
    SQLALCHEMY_DATABASE_URI ='postgres://moringa:123@localhost:5432/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY = 'my12345key67890secret'

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



class ProdConfig(Config):


    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blogs'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}