import unittest

from app.models import Source


class SourceTest(unittest.TestCase):

    def setUp(self):

        self.new_source = Source( 9090, 'abc', 'an app is about to come to life', 'https://newsapi.org/v1/sources', 'sport', 'en', 'au')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))
