from test_wework.Utils.utils import Utils


class BaseApi:
    proxies = {
        "http":"http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888"
    }
    def printResponse(self,json_object):
        print("****************log***************")
        print(Utils.jsonFormat(json_object))
        print("****************log***************")

