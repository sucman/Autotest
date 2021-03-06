# -*- coding: utf-8 -*-
import unittest
import ddt

from com.zb.control.test_assert import AssertOperation
from com.zb.control.test_datasource import Datasource
from com.zb.control.test_report import LogSeting
from com.zb.control.test_requests import RequestsControl


@ddt.ddt
class Products(unittest.TestCase):
    def setUp(self):
        pass

    @ddt.data(*Datasource.get_excel_data("../testdata/productdetail.xlsx"))
    # @ddt.unpack
    @LogSeting.casename
    def test_productdetail(self, data):
        requsts_info = Datasource.get_request_info("productdetail", data)  # db里面取接口请求方法，url，json，并用excel关键字替换模版json
        rc = RequestsControl(requsts_info)  # 实例化请求
        result = rc.request_test()  # 发送请求并拿到response
        ao = AssertOperation(result)  # 实例化断言
        ao.assert_status_code()  # 判断状态码
        ao.assert_response_node_not_null("$..duration")  # 判断某字段非空

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
