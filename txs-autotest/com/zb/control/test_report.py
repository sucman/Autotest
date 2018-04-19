# -*- coding: utf-8 -*-
# 报告

import HTMLTestRunnerCN
import logging

import time


class HtmlReport(object):
    def __init__(self):
        pass

    @staticmethod
    def html_report(testsuite):
        fp = open('index.html', 'wb')
        runner = HTMLTestRunnerCN.HTMLTestRunner(
            stream=fp,
            title='TXS Test Report',
            description='Testcase')
        runner.run(testsuite)
        fp.close()


class LogSeting:
    def __init__(self):
        pass

    @staticmethod
    def log_init():
        log_name = "log" + str(time.strftime("-%Y%m%d-%H%M%S", time.localtime())) + ".log"
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=log_name,
                            filemode='w')
