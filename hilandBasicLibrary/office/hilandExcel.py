"""
 * @file   : hilandExcel.py
 * @time   : 20:44
 * @date   : 2021/11/9
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

import xlwings as xw

from hilandBasicLibrary.office.hilandSheet import HilandSheet


class HilandExcel:
    def __init__(self, filename=None, visible=False):
        """
        在内存中打开指定的 excel 文件，或者在内存中新建一个不跟物理文件对应 excel
        :param filename: 一个物理存在的文件全名称，或者为空（但不能为物理上不存在的文件名称）
        :param visible:
        """
        app = xw.App(visible=visible, add_book=False)
        if filename:
            workbook = app.books.open(filename)
        else:
            workbook = app.books.add()

        self.workbook = workbook
        self.filename = filename
        self.app = app

    def save(self, path=""):
        """
        保存
        :param path:
        :return:
        """
        if path:
            self.workbook.save(path)
        else:
            self.workbook.save()
        return

    def close(self, save=True):
        """
        关闭 + 默认保存当前
        :param save:
        :return:
        """
        if save:
            self.workbook.save()

        self.workbook.close()
        self.app.quit()
        return

    def get_sheets_count(self):
        """
        获取电子表格的数目
        :return:
        """
        return len(self.workbook.sheets)

    def get_sheets(self):
        """
        获取所有的电子表格
        :return:
        """
        sheet_list = []
        num = len(self.workbook.sheets)
        for i in range(num):
            sht = self.workbook.sheets[i]
            sheet_list.append(HilandSheet(sht))

        return sheet_list

    def get_sheet(self, sheet_marker=None):
        """
        获取 Sheet 表格
        :param sheet_marker:sheet 表格的标识：可以是以 0 为起始的数字索引，也可以是 sheet 的名称字符串。
        :return:
        """
        if sheet_marker:
            original_sheet = self.workbook.sheets[sheet_marker]
        else:
            original_sheet = self.workbook.sheets[0]

        hiland_sheet = HilandSheet(original_sheet)
        return hiland_sheet

    # 增加sheet
    def add_sheet(self, sheet_name):
        if sheet_name:
            self.workbook.sheets.add(sheet_name, location=None, relative="before")
        else:
            self.workbook.sheets.add()
        return

    # 删除sheet
    def remove_sheet(self, sheet_marker):
        self.workbook = self.workbook.sheets[sheet_marker].delete()
        self.workbook.save()
        return self.workbook

    # sheet重命名
    def rename_sheet(self, old_sheet_marker, new_sheet_name):
        self.workbook.sheets[old_sheet_marker].name = new_sheet_name
        return self.workbook
