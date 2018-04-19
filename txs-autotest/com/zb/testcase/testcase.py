# -*- coding: utf-8 -*-
import unittest
import ddt

from com.zb.control.test_assert import AssertOperation
from com.zb.control.test_datasource import Datasource
from com.zb.control.test_requets import RequetsControl


@ddt.ddt
class Pubapi_1(unittest.TestCase):
    def setUp(self):
        pass

    @ddt.data(*Datasource.get_excel_data("pubapi_banner_all.xlsx"))
    def test_pubapi_banner_all(self, data):
        url = data[1]
        result = RequetsControl.get_test(url)
        assert_result = AssertOperation(result)
        assert_result.assert_status_code()
        assert_result.assert_response_node_not_null("$..logoPic")

    @ddt.data(*Datasource.get_excel_data("pubapi_swhz_banner.xlsx"))
    def test_pubapi_swhz_banner(self,data):
        url = data[1]
        result = RequetsControl.get_test(url)
        assert_result = AssertOperation(result)
        assert_result.assert_status_code()
        assert_result.assert_response_node_not_null("$..picUrl")
        pass

    def tearDown(self):
        pass
