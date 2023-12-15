"""

"""
from BasicLibrary.office.excelBookMate import ExcelBookMate

# TODO:xiedali@2022/3/14 使用回调完善 ExcelHelper 功能
from BasicLibrary.office.excelMisc import _calc_cell_marker
from BasicLibrary.office.excelMisc import _calc_column_name
from BasicLibrary.office.excelMisc import _calc_range_marker


class ExcelHelper:
    """

    """

    @classmethod
    def operate(cls, file_full_name, callback_in_book_mate, *args, **kwargs):
        """
        对 Excel 文件的 book 进行地快捷操作（operate_book 方法的别名）
        :param file_full_name: Excel 文件带路径的全名称
        :param callback_in_book_mate: 对 Excel 文件进行操作的回调方法。此方法要求一个类型为 ExcelBookMate 的输入参数。
        :return:
        """
        cls.operate_book(file_full_name, callback_in_book_mate, *args, **kwargs)

    @staticmethod
    def operate_book(file_full_name, callback_in_book_mate, *args, **kwargs):
        """
        对 Excel 文件的 book 进行地快捷操作
        :param file_full_name: Excel 文件带路径的全名称
        :param callback_in_book_mate: 对 Excel 文件进行操作的回调方法。此方法要求一个类型为 ExcelBookMate 的输入参数。
        :return:
        """
        with ExcelBookMate(file_full_name) as excel:
            callback_in_book_mate(excel, *args, **kwargs)

    @staticmethod
    def operate_sheet(file_full_name, callback_in_sheet_mate, sheet_marker=0, *args, **kwargs):
        """
        对 Excel 文件的 sheet 进行地快捷操作
        :param sheet_marker: sheet 的标识（sheet 索引号index 或者 sheet 的名称）
        :param file_full_name: Excel 文件带路径的全名称
        :param callback_in_sheet_mate: 对 Excel 文件的 sheet 进行操作的回调方法。此方法要求一个类型为 ExcelSheetMate 的输入参数。
        :return:
        """
        with ExcelBookMate(file_full_name) as excel:
            sheet = excel.get_sheet(sheet_marker)
            callback_in_sheet_mate(sheet, *args, **kwargs)

    @staticmethod
    def calc_column_name(start_column_name, delta):
        return _calc_column_name(start_column_name, delta)

    @staticmethod
    def calc_cell_marker(original_cell_marker, row_delta, column_delta):
        return _calc_cell_marker(original_cell_marker, row_delta, column_delta)

    @staticmethod
    def calc_range_marker(original_range_marker, row_delta, column_delta):
        return _calc_range_marker(original_range_marker, row_delta, column_delta)
