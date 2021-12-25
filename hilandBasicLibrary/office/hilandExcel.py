"""
 * @file   : hilandExcel.py
 * @time   : 20:44
 * @date   : 2021/11/9
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from builtins import *

import xlwings as xw


class HilandExcel:
    def __init__(self, filename=None, visible=False):
        app = xw.App(visible=visible, add_book=False)
        if filename:
            workbook = app.books.open(filename)
        else:
            workbook = app.books.add()

        self.workbook = workbook
        self.filename = filename
        # self.originalSheets = workbook.sheets
        # self.hilandSheets = None

    # 保存
    def save(self, path):
        if path:
            self.workbook.save(path)
        else:
            self.workbook.save()
        return

    # 关闭+默认保存当前
    def close(self, save=True):
        self.workbook.close(save=True)
        return

    # sheets列表
    def get_original_sheets(self):
        return self.workbook.sheets

    def get_hiland_sheets(self):
        sheet_list = []
        num = len(self.workbook.sheets)
        for i in range(num):
            sht = self.workbook.sheets[i]
            sheet_list.append(HilandSheet(sht))
        return sheet_list

    def get_sheets(self):
        """
        get_hiland_sheets 的别名
        :return:
        """
        return self.get_hiland_sheets()

    # 增加sheet
    def add_sheet(self, sheet_name):
        if sheet_name:
            self.workbook.sheets.add(sheet_name, location=None, relative="before")
        else:
            self.workbook.sheets.add()
        return

    # 获取sheet
    def get_original_sheet(self, sheet_marker=None):
        if sheet_marker:
            original_sheet = self.workbook.sheets[sheet_marker]
        else:
            original_sheet = self.workbook.activate
        return original_sheet

    def get_hiland_sheet(self, sheet_marker=None):
        original_sheet = self.workbook.sheets[sheet_marker]
        hiland_sheet = HilandSheet(original_sheet)
        return hiland_sheet

    def get_sheet(self, sheet_marker=None):
        """
        get_hiland_sheet 的别名
        :param sheet_marker:
        :return:
        """
        return self.get_hiland_sheet(sheet_marker)

    # 删除sheet
    def remove_sheet(self, sheet_marker):
        self.workbook = self.workbook.sheets[sheet_marker].delete()
        self.workbook.save()
        return self.workbook

    # sheet重命名
    def rename_sheet(self, old_sheet_marker, new_sheet_name):
        self.workbook.sheets[old_sheet_marker].name = new_sheet_name
        return self.workbook
