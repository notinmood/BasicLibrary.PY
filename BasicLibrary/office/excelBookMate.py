"""
 * @file   : hilandExcel.py
 * @time   : 20:44
 * @date   : 2021/11/9
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

import xlwings as xw

from BasicLibrary import ObjectHelper
from BasicLibrary.office.excelSheetMate import ExcelSheetMate


class ExcelBookMate:
    """

    """

    def __init__(self, filename=None, visible=False):
        """
        在内存中打开指定的 excel 文件，或者在内存中新建一个不跟物理文件对应 excel
        :param filename: 一个物理存在的文件全名称，或者为空。但不能为物理上不存在的文件名称。
        :param visible:
        """
        app = xw.App(visible=visible, add_book=False)
        if filename:
            workbook = app.books.open(filename)
        else:
            workbook = app.books.add()

        # 不推荐使用 xw.Book(filename)，容易多个线程占用文件
        # workbook = xw.Book(filename)

        self.workbook = workbook
        self.filename = filename
        self.app = app
        """
        当前被选中的表格的区域
        """
        self.range_selected = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

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
        if self.workbook:
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
        return self.workbook.sheets.count

    def get_sheets(self):
        """
        获取所有的电子表格
        :return:
        """
        sheet_list = []
        num = len(self.workbook.sheets)
        for i in range(num):
            sht = self.workbook.sheets[i]
            sheet_list.append(ExcelSheetMate(sht))

        return sheet_list

    def get_sheet(self, sheet_marker=None):
        """
        获取 Sheet 表格
        :param sheet_marker:sheet 表格的标识：
            1. 可以是 sheet 的名称字符串。
            2. 可以是以 0 为起始的数字索引.如果索引号超出最大范围，就取最后一个表格。
        :return:
        """
        marker_type = ObjectHelper.get_type(sheet_marker)
        if marker_type is int:
            if sheet_marker < 0:
                sheet_marker = 0
            else:
                sheets_count = self.get_sheets_count()
                if sheet_marker >= sheets_count:
                    sheet_marker = sheets_count - 1

        if sheet_marker:
            original_sheet = self.workbook.sheets[sheet_marker]
        else:
            original_sheet = self.workbook.sheets[0]

        hiland_sheet = ExcelSheetMate(original_sheet)
        return hiland_sheet

    def determine_exist_sheet(self, sheet_marker):
        """
        判断是否存在某个 sheet
        :param sheet_marker:
        :return:
        """
        marker_type = ObjectHelper.get_type(sheet_marker)
        if marker_type == int:
            all_count = self.get_sheets_count()
            if 0 <= sheet_marker < all_count:
                return True

        if marker_type == str:
            for sheet in self.get_sheets():
                if sheet.get_name() == sheet_marker:
                    return True

        # 其他情况都视为不存在这样的表格
        return False

    def add_sheet(self, sheet_name, index=-1):
        """
        增加 sheet
        :param sheet_name: 新添加表的名称
        :param index: 新添加表的位置索引号(默认为 -1：插入点到当前各存量表的最后面)
        :return:
        """
        sheets_count = self.get_sheets_count()
        position = index

        if index < 0:
            position = sheets_count

        if (position is not None) and (position >= sheets_count):
            position = sheets_count

        if sheet_name:
            if position == 0:
                new_sheet = self.workbook.sheets.add(sheet_name, before=1)
            else:
                new_sheet = self.workbook.sheets.add(sheet_name, after=position)
        else:
            new_sheet = self.workbook.sheets.add()

        if new_sheet:
            return ExcelSheetMate(new_sheet)
        else:
            return None

    def remove_sheet(self, sheet_marker):
        """
        删除sheet(由于 Excel 本身的限制，如果一个工作簿仅剩余一个 sheet 的时候，本方法无法将其删除)
        :param sheet_marker:
        :return:
            删除成功返回 True；
            删除失败返回 False：sheet_marker 不存在或者 一个工作簿仅剩余一个 sheet 的时候继续删除 都会返回失败。
        """
        is_exist = self.determine_exist_sheet(sheet_marker)
        if is_exist and self.get_sheets_count() > 1:
            self.workbook.sheets[sheet_marker].delete()
            self.workbook.save()
            return True
        else:
            return False

    def rename_sheet(self, sheet_old_marker, sheet_new_name):
        """
        sheet重命名
        :param sheet_old_marker:
        :param sheet_new_name:
        :return:
        """
        is_exist = self.determine_exist_sheet(sheet_old_marker)
        if is_exist and self.get_sheets_count() > 1:
            self.workbook.sheets[sheet_old_marker].name = sheet_new_name
            self.workbook.save()
            return True
        else:
            return False

    def copy(self, sheet_marker, range_marker):
        """
        复制
        :param sheet_marker:
        :param range_marker:
        :return:
        """
        sheet = self.get_sheet(sheet_marker)
        if sheet:
            self.range_selected = sheet.original_sheet.range(range_marker).value

        return self.range_selected

    def paste(self, sheet_marker, range_marker, range_data=None):
        """
        粘贴
        :param sheet_marker:
        :param range_marker:
        :param range_data:
        :return:
        """
        if not range_data:
            range_data = self.range_selected

        sheet = self.get_sheet(sheet_marker)
        if sheet:
            sheet.original_sheet.range(range_marker).value = range_data

        return
