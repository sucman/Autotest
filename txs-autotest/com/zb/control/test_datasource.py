# -*- coding: utf-8 -*-
import logging
import pymysql
from openpyxl import *

from com.zb.control import config


class Datasource():
    def __init__(self):
        pass

    @staticmethod
    def get_excel_data(excel_name):
        wb = load_workbook(excel_name)
        ws = wb[wb.sheetnames[0]]
        case_list = []
        for i in range(2, ws.max_row + 1):
            list_temp = []
            for j in range(1, ws.max_column + 1):
                list_temp.append(ws.cell(row=i, column=j).value)
            case_list.append(list_temp)
            # yield list_temp
        return case_list

    # 连db
    @staticmethod
    def get_interface_template(interface_name):
        try:
            db = pymysql.connect(host=config.DB_HOST, port=config.DB_PORT, user=config.DB_USER, password=config.DB_PWD,
                                 db=config.DB_DATABASE, charset='utf8')
        except Exception, dberr:
            logging.error("connect da error:%s" % dberr)
            return
        cu = db.cursor()
        cu.execute("SELECT a.type,a.url,a.json FROM interface_template a WHERE a.interface_name=%s", interface_name)
        # db.commit()
        result = cu.fetchall()[0]
        result = list(result)
        db.close()
        return result
