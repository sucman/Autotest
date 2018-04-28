# -*- coding: utf-8 -*-
import unittest
import ddt

from com.zb.control.test_assert import AssertOperation
from com.zb.control.test_datasource import Datasource
from com.zb.control.test_requests import RequestsControl


@ddt.ddt
class Products(unittest.TestCase):
    def setUp(self):
        pass

    @ddt.data(*Datasource.get_excel_data("../testdata/productdetail.xlsx"))
    def test_productdetail(self,data):
        data1 = data
        print data1
        requsts_info = Datasource.get_interface_template("productdetail")  # db里面取接口请求方法，url，json
        rc = RequestsControl(requsts_info)  # 实例化请求
        result = rc.request_test()  # 发送请求并拿到response
        print result
        ao = AssertOperation(result)  # 实例化断言
        ao.assert_status_code()  # 判断状态码
        # ao.assert_response_node_not_null("$..picUrl")  # 判断某字段非空

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
