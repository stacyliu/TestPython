from unittest import TestCase

from test_wework.api.message import Message


class TestMessage(TestCase):
    sendmessage=Message()

    def test_send_text(self, tousers=["wsygxmj","24103671"], parties=[], tags=[]):
        print(self.sendmessage.send_text(tousers, parties, tags))
        assert self.sendmessage.send_text(tousers, parties, tags).get("errmsg")=='ok'
        assert self.sendmessage.send_text(tousers, parties, tags).get("errcode")==0

