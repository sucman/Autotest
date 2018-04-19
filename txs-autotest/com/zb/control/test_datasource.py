# -*- coding: utf-8 -*-
import logging

from openpyxl import *

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

