# -*- coding: utf-8 -*-
import requests
import json
import jsonpath


class AssertOperation():
    def __init__(self, res):
        self.__res = res

    ##判断http响应码为200
    def assert_status_code(self):
        assert self.__res.status_code == 200

    ##判断返回值的某节点有值
    def assert_response_node_not_null(self, path):
        response_type = json.loads(self.__res.text)
        node_values = jsonpath.jsonpath(response_type, path)
        print node_values
        assert len(node_values) >= 1

    ##判断返回值的某节点值与预期结果是否一直
    def assert_response_values(self, path,expected_result):
        response_type = json.loads(self.__res.text)
        node_values = jsonpath.jsonpath(response_type, path)
        assert node_values == expected_result



