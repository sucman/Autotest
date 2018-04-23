# -*- coding: utf-8 -*-
# 报告

import HTMLTestRunnerCN
import logging
import smtplib

import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from com.zb.control import config



class HtmlReport(object):
    def __init__(self):
        pass

    @staticmethod
    def html_report(testsuite,tester="pengjunjie"):
        fp = open('../../../index.html', 'wb')
        runner = HTMLTestRunnerCN.HTMLTestRunner(
            stream=fp,
            title='TXS Autotest Report',
            description='txs autotest for demo',
            tester=tester)
        runner.run(testsuite)
        fp.close()


class Email:
    def __init__(self):
        pass

    def get_report_info(self):
        info = ""
        with open('../../../index.html', 'rb') as f:
            for line in f.readlines():
                if line.find("<p class='attribute'><strong>") >= 0:
                    info = info + line
        return info

    def send_email(self):
        mail_host = config.MAIL_HOST  # 设置服务器
        mail_user = config.MAIL_USER  # 用户名
        mail_pass = config.MAIL_PWD  # 口令
        sender = config.MAIL_SENDER
        receivers = config.MAIL_RECEIVERS  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        subject = '自动化测试报告 ' + str(time.strftime("%Y%m%d %H:%M:%S", time.localtime()))
        mail_msg = '<h2 style="font-family: Microsoft YaHei">TXS Autotest Report</h2>\n' + self.get_report_info() + '<p><a href="http://192.168.0.78:8080/autotest/index.html">点击此处查看详细报告</a> </p>'
        message = MIMEMultipart()
        message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
        # message = MIMEText('自动化测试报告', 'plain', 'utf-8')
        message['From'] = Header(mail_user)
        message['To'] = Header(",".join(config.MAIL_RECEIVERS))
        message['Subject'] = Header(subject, 'utf-8')

        # 构造附件
        att1 = MIMEText(open('../../../index.html', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="report.html"'
        message.attach(att1)

        smtpObj = smtplib.SMTP(mail_host, 25)
        # smtpObj.set_debuglevel(1)
        smtpObj.starttls()
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()


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

