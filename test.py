import unittest
from main import app
import logging
import sys


class TestMainClass(unittest.TestCase):
    LIST_OF_ENDPOINTS = ['/', '/home', '/about', '/artwork', '/news',
                         '/publications', '/services', '/forum', '/contact']
    NUMBER_OF_NON_STATIC_EXPOSED_ENDPOINTS = 9

    def test_non_static_endpoint_response_200(self):
        # log = logging.getLogger()
        tester = app.test_client()
        for url_map in app.url_map.iter_rules():
            endpoint = '/' + url_map.endpoint
            # log.debug(url_map)
            if 'static' not in endpoint:
                self.assertEqual(tester.get(endpoint, content_type='html/text').status_code, 200,
                                 'response of "{}" endpoint is not 200'.format(endpoint))

    def test_number_of_exposed_non_static_endpoints(self):
        number_of_endpoints = 0
        for url_map in app.url_map.iter_rules():
            endpoint = '/' + url_map.endpoint
            if 'static' not in endpoint:
                number_of_endpoints = number_of_endpoints + 1
        self.assertEqual(number_of_endpoints, self.NUMBER_OF_NON_STATIC_EXPOSED_ENDPOINTS)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
