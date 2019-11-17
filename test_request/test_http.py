import json

import requests
import pytest
from requests import Response
from jsonschema import validate



class TestHttp:
    def test_get(self):
        res = requests.get('http://m.fanfou.com')
        self.inspect_reqponse(res)

    def test_get_with_patams(self):
        url = 'http://httpbin.org/get'
        request_params = {"k1": "11111", "k2": "22222"}
        res = requests.get(url, params=request_params)
        self.inspect_reqponse(res)

    def test_get_with_params_headers(self):
        url = 'http://httpbin.org/get'
        request_params = {"k1": "11111", "k2": "22222"}
        request_headers = {"h1": "aaaaaa", "h2": "bbbb"}
        res = requests.get(url, params=request_params,headers=request_headers)
        self.inspect_reqponse(res)

    def test_post_with_data_headers(self):
        url="http://httpbin.org/post"
        request_params = {"k1": "11111", "k2": "22222"}
        request_forms={"f1":"form1","f2":"form2"}
        request_headers = {"h1": "aaaaaa", "h2": "bbbb"}
        request_proxy={"http":"10.92.213.29:8888"} #通过charles抓包 就能抓到这一条请求 没啥用 方便调试
        res= requests.post(url,data=request_forms,params=request_params,proxies=request_proxy,headers=request_headers)
        self.inspect_reqponse(res)

    def test_testerhome_url_json(self):
        url = "https://testerhome.com/api/v3/topics.json"
        request_params={"limit":"2"}
        res = requests.get(url,params=request_params)
        print(res.json()["topics"][-1]['user']["login"])
        assert res.json()["topics"][-1]['user']["login"]!=None

    def test_testerhome_url_jsonscheme(self):
        url = "https://testerhome.com/api/v3/topics.json"
        request_params={"limit":"2"}
        res = requests.get(url,params=request_params)
        my_json_schema = json.load(open('my_json_schema.json'))
        print(my_json_schema)
        print(res.json())
        validate(res.json(), schema=my_json_schema)



    def inspect_reqponse(self,res:Response):
        print(res.content)
        print("********************")
        print(res.headers)
        print("********************")
        print(res.raw)
        print("********************")
        print(res.cookies)
        print("********************")
        print(res.status_code)
        print("********************")
        print(res.url)
        print("********************")
        print(res.text)
        print("********************")
        print(res.encoding)
        print("********************")
        print(res.json())
        print("********************")
