# -*- coding: utf-8 -*-

import unittest
import os

from com.zb.control.test_report import HtmlReport
from com.zb.testcase.testcase import *


def runner_main():

    suite = unittest.TestLoader().loadTestsFromTestCase(Pubapi_1)
    # unittest.TextTestRunner(verbosity=2).run(suite)

    HtmlReport.html_report(suite)


runner_main()