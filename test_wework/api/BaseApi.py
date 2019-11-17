from test_wework.Utils.utils import Utils


class BaseApi:
    def printResponse(self,json_object):
        print("****************log***************")
        print(Utils.jsonFormat(json_object))
        print("****************log***************")