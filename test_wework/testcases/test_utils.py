from unittest import TestCase

import requests

from test_wework.Utils.utils import Utils
from test_wework.api.department import Department


class TestUtils(TestCase):
    department = Department()
    def test_jsonFormat(self):
        print(Utils.jsonFormat(self.department.list('2')))

    def test_jsonFormat(self):
        print(requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json())
        print((Utils.jsonFormat(requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json())))
