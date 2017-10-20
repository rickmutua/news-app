class Config:

    SOURCE_API_BASE_URL = 'https://newsapi.org/v1/sources?category={}'


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True