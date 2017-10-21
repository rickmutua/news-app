class Source:

    def __init__(self, id, name, description, url, category, language, country, urlsToLogos):

        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        self.urlsToLogos = urlsToLogos


class Article:

    def __init__(self, author, title, description, url, urlToImage,  publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt