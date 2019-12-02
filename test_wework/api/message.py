import requests

from test_wework.api.wework import WeWork


class Message:
    _send_url="https://qyapi.weixin.qq.com/cgi-bin/message/send"
    def send_text(self, tousers,parties,tags):
        send_json={
                       "touser" : "|".join(tousers),
                       "toparty" : "|".join(parties),
                       "totag" : "|".join(tags),
                       "msgtype" : "text",
                       "agentid" : WeWork.agent_id,
                       "text" : {
                           "content" : "你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"
                       },
                       "safe":0,
                       "enable_id_trans": 0
                    }
        params = {'access_token': WeWork.get_accesstoken_app()}
        #print(WeWork.get_accesstoken_app())
        return requests.post(url=self._send_url,json=send_json,params=params).json()
