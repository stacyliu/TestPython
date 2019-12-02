import requests


class WeWork:
    corpid="ww2b997648c2ee96aa"
    agent_id="3010011"
    agent_secret="pLZn6i5vgijt2RAsDgWVTRS3l8CMco1Mqs_B2APFzkY"
    contract_secret="CGaWzvkCD9mNUhy_k08FK7RLvrRI18_j9zzytUt4Pno"
    access_token_contact=None
    access_token_app=None

    @classmethod
    def get_accesstoken_contact(cls):
        if(cls.access_token_contact==None):
            url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            params={'corpid':cls.corpid,'corpsecret':cls.contract_secret}
            response_json=requests.request("GET", url, params=params).json()
            if(response_json.get('access_token')!=None):
                WeWork.access_token_contact=response_json.get('access_token')
            #print('1')
            return WeWork.access_token_contact
        else:
            #print('2')
            return WeWork.access_token_contact

    @classmethod
    def get_accesstoken_app(cls):
        if (cls.access_token_app == None):
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            params = {'corpid': cls.corpid, 'corpsecret': cls.agent_secret}
            response_json = requests.request("GET", url, params=params).json()
            if (response_json.get('access_token') != None):
                WeWork.access_token_app = response_json.get('access_token')
            #print('1')
            return WeWork.access_token_app
        else:
            #print('2')
            return WeWork.access_token_app


