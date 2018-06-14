# -*- coding: UTF-8 -*-
"""
A simple test suite to ensure the new repo is functional
"""
import unittest

from vlab_links_api.lib.constants import const


class TestLinksApp(unittest.TestCase):
    """A simple test to verify repo functionality"""

    def test_known_constants(self):
        """All constants are known"""
        expected = ['LINKS_LOG_LEVEL', 'LINKS_MAX_COUNT', 'VLAB_URL']
        for item in expected:
            self.assertTrue(hasattr(const, item))


if __name__ == '__main__':
    unittest.main()
