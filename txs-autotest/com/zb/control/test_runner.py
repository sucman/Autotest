# -*- coding: utf-8 -*-
import logging
import unittest
import os

from com.zb.control.test_report import HtmlReport, Email
from com.zb.testcase.testcase_products import Products
from com.zb.testcase.testcase_pubapi import *


def runner_main():
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Pubapi)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Products)
    # unittest.TextTestRunner(verbosity=2).run(suite)

    alltests = unittest.TestSuite((suite1, suite2))
    HtmlReport.html_report(alltests)


LogSeting.log_init()
runner_main()
send_mail = Email()
send_mail.send_email()
