# -*- coding: utf-8 -*-

import unittest
import os

from com.zb.control.test_report import HtmlReport, Email
from com.zb.testcase.testcase import *


def runner_main():
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Pubapi_1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase()

    # unittest.TextTestRunner(verbosity=2).run(suite)
    alltests = unittest.TestSuite(suite1)
    HtmlReport.html_report(alltests)


runner_main()
send_mail = Email()
send_mail.send_email()
