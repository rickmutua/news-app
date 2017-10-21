import os


class Config:

    API_KEY = os.environ.get('API_KEY')

    SOURCE_API_BASE_URL = 'https://newsapi.org/v1/sources?category={}'

    ARTICLES_API_BASE_URL = 'https://newsapi.org/v1/articles?source={}&apiKey={}'


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}