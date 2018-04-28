# -*- coding: utf-8 -*-
import logging
import requests
import json


class RequestsControl():
    def __init__(self, request_info, mobile=0):
        self.__request_info = request_info
        self.__mobile = mobile
        pass

    def post_test(self):
        headers = {'content-type': 'application/json'}
        data = self.__request_info[2]
        data = json.loads(data)
        try:
            logging.info("http post url: %s" % self.__request_info[1])
            logging.info("http request: %s" % data)
            res = requests.post(self.__request_info[1], json=data, headers=headers)
            logging.info("http response: %s " % res.text)
            return res
        except Exception, e:
            logging.error("http error:%s" % e)

    def get_test(self):
        try:
            logging.info("http get url: %s" % self.__request_info[1])
            res = requests.get(url=self.__request_info[1])
            logging.info("http response: %s " % res.text)
            return res
        except Exception, e:
            logging.error("http error:%s" % e)
            # return

    ###判断请求是get还是post
    ### 是否需要先获取cookie
    def request_test(self):
        if self.__request_info[0] == 0:
            return self.get_test()
        elif self.__request_info[0] == 1:
            return self.post_test()
            # if self.__iscookie != 0:
            #     #调用需要待cookie的post请求
            #     pass
