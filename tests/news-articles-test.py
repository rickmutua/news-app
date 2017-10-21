import unittest

from app.models import articles

Articles = articles.Article


class ArticlesTest(unittest.TestCase):

    def setUp(self):

        self.new_article = Articles('Tim', 'see your life', 'a story on how someone sow their lifes', 'https://newsapi.org/v1/articles?source=techcrunch&apiKey=f46b7b733c3841b68374e491c88ee96e', 'https://tctechcrunch2011.files.wordpress.com/2015/03/tccrshowogo.jpg?w=500&h=200&crop=1', '2017-10-20T09:18:14Z')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_article, Articles))


if __name__ == '__main__':
    unittest.main()