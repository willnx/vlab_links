# -*- coding: UTF-8 -*-
"""
A simple set of tests for the health check functionality.
"""
import unittest

import vlab_link_api.app as link_app


class TestHealthView(unittest.TestCase):
    """A suite of test cases for the /api/1/link/healthcheck end point"""

    def setUp(self):
        """Runs before every test case"""
        link_app.app.config['TESTING'] = True
        self.app = link_app.app.test_client()

    def test_works(self):
        """Verify the healthcheck happy path works"""
        resp = self.app.get('/api/1/link/healthcheck')
        expected = 200

        self.assertEqual(resp.status_code, expected)


if __name__ == '__main__':
    unittest.main()
