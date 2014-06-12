""" Tests for debian tools. """
import json
import unittest
from python_deb_tools.versions import get_version_list, get_version_list_json


class TestVersionFunctions(unittest.TestCase):
    """ Tests for Version functions """

    def test_get_version_list(self):
        """ Test the get version functions """
        version_dict = get_version_list()
        version_json = get_version_list_json()
        self.assertIsNotNone(version_dict)
        self.assertEquals(len(version_dict), 634)
        self.assertIsNotNone(version_json)
        temp = json.loads(version_json)
        self.assertEquals(len(temp), 634)
