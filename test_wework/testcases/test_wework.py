from unittest import TestCase

from test_wework.api import wework
from test_wework.api.wework import WeWork


class TestWeWork(TestCase):
    def test_get_accesstoken(self):
        wework=WeWork()
        assert wework.get_accesstoken_contact() != None