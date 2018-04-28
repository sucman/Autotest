# -*- coding: utf-8 -*-

import requests
import json

from com.zb.control.test_assert import AssertOperation
from com.zb.control.test_datasource import Datasource


class RequestsControl():
    def __init__(self,request_info,iscookie = 0):
        self.__request_info = request_info
        self.__iscookie = iscookie
        pass

    def post_test(self):
        headers = {'content-type': 'application/json'}
        data =self.__request_info[2]
        print type(data)
        print data
        data = json.loads(data)
        print type(data)
        print data
        ####
        data["productid"]="dfdfdfdf"
        print type(data)
        print data
        ####
        res = requests.post(self.__request_info[1], json=data, headers=headers)
        return res

    def get_test(self):
        # print self.__request_info[1]
        res = requests.get(url=self.__request_info[1])
        return res

    def request_test(self):
        if self.__request_info[0]==0:
            return self.get_test()
        elif self.__request_info[0]==1:
            return self.post_test()
            # if self.__iscookie != 0:
            #     #调用需要待cookie的post请求
            #     pass



if __name__ == '__main__':
    # dd = [1,"https://tservice.txslicai.com/StoreServices.svc/product/productdetail",'{"productid":"968732659754864640","bid":""}']
    # rc = RequestsControl(dd)
    # a = rc.post_test()
    # print a

    di = {"productid":"968732659754864640","bid":{"aa":11,"bb":"bb"}}
    print type(di)
    di["productid"]="ddd"
    di["bid"]["aa"]=3
    print di