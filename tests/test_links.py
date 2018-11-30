# -*- coding: UTF-8 -*-
"""
Suite(s) of unit tests for the /api/1/link API
"""
import unittest
from unittest.mock import patch

import ujson
from vlab_api_common import flask_common
from vlab_api_common.http_auth import generate_v2_test_token
from jsonschema import Draft4Validator, validate

import vlab_link_api.app as link_app
from vlab_link_api.lib.views import link


class TestLinkView(unittest.TestCase):
    """A suite of test cases for the /api/1/link end point"""

    @classmethod
    def setUpClass(cls):
        """Runs once, before any test case"""
        cls.auth_token = generate_v2_test_token(username='bob')

    def setUp(self):
        """Runs before every test case"""
        link_app.app.config['TESTING'] = True
        self.app = link_app.app.test_client()

    def test_post_schema(self):
        """The schema defined for POST on /api/1/link is valid"""
        try:
            Draft4Validator.check_schema(link.LinkView.POST_SCHEMA)
            schema_valid = True
        except RuntimeError:
            schema_valid = False

        self.assertTrue(schema_valid)

    def test_post_success_status_code(self):
        """POST on /api/1/link returns a 200 upon success"""
        payload = {'url' : 'http://some.url.com'}
        resp = self.app.post('/api/1/link',
                             data=ujson.dumps(payload),
                             content_type='application/json',
                             headers={'X-Auth' : self.auth_token})
        expected = 200

        self.assertEqual(resp.status_code, expected)

    def test_post_success_data(self):
        """POST on /api/1/link returns the expected content data"""
        payload = {'url' : 'http://some.url.com'}
        resp = self.app.post('/api/1/link',
                             data=ujson.dumps(payload),
                             content_type='application/json',
                             headers={'X-Auth' : self.auth_token})
        content = ujson.loads(resp.data)['content']
        expected = {'lid': '3a628d13f6c4e4f325408da0153e3c87',
                    'url': 'https://localhost/api/1/link/3a628d13f6c4e4f325408da0153e3c87'}

        self.assertEqual(content, expected)

    @patch.object(flask_common, 'logger')
    def test_post_no_body(self, fake_logger):
        """POST on /api/1/link returns a 400 if not supplied with any body content"""
        resp = self.app.post('/api/1/link',
                             data=ujson.dumps({}),
                             content_type='application/json',
                             headers={'X-Auth' : self.auth_token})
        expected = 400

        self.assertEqual(resp.status_code, expected)

    @patch.object(flask_common, 'logger')
    def test_post_invalid_body(self, fake_logger):
        """POST on /api/1/link returns a 400 if supplied with invalid body content"""
        payload = {'doh' : ['http://some.url.com']}
        resp = self.app.post('/api/1/link',
                             data=ujson.dumps(payload),
                             content_type='application/json',
                             headers={'X-Auth' : self.auth_token})
        expected = 400

        self.assertEqual(resp.status_code, expected)

    def test_get_no_link(self):
        """GET on /api/1/link/<lid> returns 404 if <lid> is not a known stored link"""
        resp = self.app.get('/api/1/link/notalink')
        expected = 404

        self.assertEqual(resp.status_code, expected)

    def test_get_link_found(self):
        """GET on /api/1/link/<lid> returns a 301 redirect when <lid> is a known stored link"""
        payload = {'url' : 'http://some.url.com'}
        resp = self.app.post('/api/1/link',
                             data=ujson.dumps(payload),
                             content_type='application/json',
                             headers={'X-Auth' : self.auth_token})
        content = ujson.loads(resp.data)['content']
        valid_link = '/api/1/link/' + content['lid']

        resp2 = self.app.get(valid_link)
        expected = 301

        self.assertEqual(resp2.status_code, expected)

    def test_get_describe(self):
        """GET on /api/1/link work when supplied with the describe param"""
        resp = self.app.get('/api/1/link?describe=true',
                            headers={'X-Auth' : self.auth_token})
        expected = 200

        self.assertEqual(resp.status_code, expected)

    def test_get_describe_no_param(self):
        """GET on /api/1/link returns 405 when not supplied with the describe param"""
        resp = self.app.get('/api/1/link',
                            headers={'X-Auth' : self.auth_token})
        expected = 405

        self.assertEqual(resp.status_code, expected)


if __name__ == '__main__':
    unittest.main()
