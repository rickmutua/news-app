import urllib.request, json
from .models import Source, Article


api_key = None

source_base_url = None

articles_base_url = None


def configure_request(app):

    global api_key, source_base_url, articles_base_url

    api_key = app.config['API_KEY']

    source_base_url = app.config["SOURCE_API_BASE_URL"]

    articles_base_url = app.config["ARTICLES_API_BASE_URL"]


def get_sources(category):

    get_sources_url = source_base_url.format(category)

    with urllib.request.urlopen(get_sources_url) as url:

        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return  source_results


def process_results(source_list):

    source_results = []

    for source_item in source_list:

        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Source(id, name, description, url, category, language, country)
        source_results.append(source_object)

    return source_results


def get_source_articles(source):

    get_articles_url = articles_base_url.format(source, api_key)

    with urllib.request.urlopen(get_articles_url, data=None) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(article_list):

    articles_results = []

    for article_item in article_list:

        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        article_object = Article(author, title, description, url, urlToImage, publishedAt)

        articles_results.append(article_object)

    return articles_results



