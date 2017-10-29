import os


class Config:

    API_KEY = os.environ.get('API_KEY')

    SOURCE_API_BASE_URL = 'https://newsapi.org/v1/sources?category={}'

    ARTICLES_API_BASE_URL = 'https://newsapi.org/v1/articles?source={}&apiKey={}'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://erick:qwerty12345@localhost/newsapp'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    pass


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://erick:qwerty12345@localhost/newsapp'

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}