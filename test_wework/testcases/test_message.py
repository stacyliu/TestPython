from unittest import TestCase

from test_wework.api.message import Message


class TestMessage(TestCase):
    sendmessage=Message()

    def test_send_text(self, tousers=["1"], parties=["1"], tags=["1"]):
        print(self.sendmessage.send_text(tousers, parties, tags))

