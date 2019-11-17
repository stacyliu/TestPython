
'''
https://work.weixin.qq.com/api/doc#90000/90135/90204
https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=ACCESS_TOKEN
'''
import requests

from test_wework.Utils.utils import Utils
from test_wework.api.wework import WeWork


class Department:
    '''
    https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=ACCESS_TOKEN&id=ID
    https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=ACCESS_TOKEN
    https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token=ACCESS_TOKEN&id=ID
    https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token=ACCESS_TOKEN
    '''

    list_url="https://qyapi.weixin.qq.com/cgi-bin/department/list"
    def list(self,*id):
        if(id.count==0):
            params={'access_token':WeWork.get_accesstoken()}
        else:
            params = {'access_token': WeWork.get_accesstoken(),'id':id}

        print(Utils.jsonFormat(requests.request("GET", self.list_url, params=params).json()))
        return(requests.request("GET", self.list_url, params=params).json())

    def create(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass