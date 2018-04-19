# -*- coding: utf-8 -*-

import requests
import json

from com.zb.control.test_assert import AssertOperation


class RequetsControl():
    def __init__(self):
        pass

    @staticmethod
    def post_test(url, data):
        pass
        headers = {'content-type': 'application/json'}
        res = requests.post(url, json=data, headers=headers)
        return res

    @staticmethod
    def get_test(url):
        pass
        res = requests.get(url=url)
        return res


if __name__ == '__main__':
    url = "https://javaapitest.txslicai.com/operation/launching_transition"
    a = RequetsControl.get_test(url)
    print a.status_code
    print a.text
    pass
