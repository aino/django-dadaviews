from django.test import TestCase
from dadaviews.base import uncamel


class UnCamelTestCase(TestCase):
    def test_basic(self):
        self.assertEqual(uncamel('CamelCase'), 'camel_case')

    def test_basic_more(self):
        self.assertEqual(uncamel('CamelCamelCase'), 'camel_camel_case')

    def test_numbers(self):
        self.assertEqual(uncamel('Camel2Camel2Case'), 'camel2_camel2_case')

    def test_begin_small(self):
        self.assertEqual(uncamel('getHTTPResponseCode'), 'get_http_response_code')

    def test_begin_small_and_numbers(self):
        self.assertEqual(uncamel('get2HTTPResponseCode'), 'get2_http_response_code')

    def test_some_big(self):
        self.assertEqual(uncamel('HTTPResponseCode'), 'http_response_code')

    def test_some_big_small_big(self):
        self.assertEqual(uncamel('HTTPResponseCodeXYZ'), 'http_response_code_xyz')
