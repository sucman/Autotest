# -*- coding: utf-8 -*-
import unittest
import ddt

from com.zb.control.test_assert import AssertOperation
from com.zb.control.test_datasource import Datasource
from com.zb.control.test_report import LogSeting
from com.zb.control.test_requests import RequestsControl


class Pubapi(unittest.TestCase):
    def setUp(self):
        pass

    @LogSeting.casename
    def test_swhz_banner(self):
        body = Datasource.get_request_info("swhz_banner")  # db里面取接口请求方法，url，json
        rc = RequestsControl(body)  # 实例化请求
        result = rc.request_test()  # 发送请求并拿到response
        ao = AssertOperation(result)  # 实例化断言
        ao.assert_status_code()  # 判断状态码
        ao.assert_response_node_not_null("$..picUrl")  # 判断某字段非空

    @LogSeting.casename
    def test_launching_transition(self):
        body = Datasource.get_request_info("launching_transition")
        rc = RequestsControl(body)
        result = rc.request_test()
        ao = AssertOperation(result)
        ao.assert_status_code()
        ao.assert_response_node_not_null("$..logoPic")

    @LogSeting.casename
    def test_new_welfare(self):
        body = Datasource.get_request_info("new_welfare")
        rc = RequestsControl(body)
        result = rc.request_test()
        ao = AssertOperation(result)
        ao.assert_status_code()
        ao.assert_response_node_not_null("$..logoPic")

    @LogSeting.casename
    def test_old_welfare(self):
        body = Datasource.get_request_info("old_welfare")
        rc = RequestsControl(body)
        result = rc.request_test()
        ao = AssertOperation(result)
        ao.assert_status_code()
        ao.assert_response_node_not_null("$..logoPic")

    @LogSeting.casename
    def test_financing_top(self):
        body = Datasource.get_request_info("financing_top")
        rc = RequestsControl(body)
        result = rc.request_test()
        ao = AssertOperation(result)
        ao.assert_status_code()
        ao.assert_response_node_not_null("$..logoPic")

    @LogSeting.casename
    def test_old(self):
        body = Datasource.get_request_info("old")
        rc = RequestsControl(body)
        result = rc.request_test()
        ao = AssertOperation(result)
        ao.assert_status_code()
        ao.assert_response_node_not_null("$..logoPic")

    @LogSeting.casename
    def test_new(self):
        body = Datasource.get_request_info("new")
        rc = RequestsControl(body)
        result = rc.request_test()
        ao = AssertOperation(result)
        ao.assert_status_code()
        ao.assert_response_node_not_null("$..logoPic")

    def tearDown(self):
        pass
