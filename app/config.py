class Config:

    SOURCE_API_BASE_URL = 'https://newsapi.org/v1/sources?category={}'

    # ARTICLE_API_BASE_URL = ' https://newsapi.org/v1/articles?source={}&sortBy=latest&apiKey={}'


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True