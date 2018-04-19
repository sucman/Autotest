# -*- coding: utf-8 -*-
import logging
import unittest
from email.mime.multipart import MIMEMultipart

if __name__ == '__main__':
    # # a = Datasource.get_excel_data("adtest.xlsx")
    # # print a
    # suite = unittest.TestLoader().loadTestsFromTestCase(Pubapi_1)
    # # unittest.TextTestRunner(verbosity=2).run(suite)
    # # print a.next()
    # # print a.next()
    # # print a.next()
    #
    #
    # # suite.addTest(Dome("test_new_welfare"))
    #
    #
    # HtmlReport.html_report(suite)
    pass

    # -*- coding: UTF-8 -*-

    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    # 第三方 SMTP 服务
    mail_host = "smtp.sina.com"  # 设置服务器
    mail_user = "pengjunjie2018@sina.com"  # 用户名
    mail_pass = "123456a"  # 口令
    sender = 'pengjunjie2018@sina.com'
    receivers =["395390646@qq.com","pengjunjie@zillionfortune.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    subject = '自动化测试报告'
    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.runoob.com">这是一个链接</a></p>
    """
    message = MIMEMultipart()
    message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    # message = MIMEText('自动化测试报告', 'plain', 'utf-8')
    message['From'] = Header(mail_user)
    # message['To'] = Header("测试", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('../../../index.html', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="index.html"'
    message.attach(att1)

    smtpObj = smtplib.SMTP(mail_host, 25)
    smtpObj.set_debuglevel(1)
    smtpObj.starttls()
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
