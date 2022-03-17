"""

"""
from hilandBasicLibrary.office.excelBookMate import ExcelBookMate

# TODO:xiedali@2022/3/14 使用回调完善 ExcelHelper 功能
from hilandBasicLibrary.office.excelMisc import _calc_column_name


class ExcelHelper:
    @staticmethod
    def calc_column_name(start_column_name, delta):
        return _calc_column_name(start_column_name, delta)

#     @staticmethod
#     def operate(file_full_name, callback):
#         with ExcelBookMate(file_full_name) as excel:
#             callback(excel)
#
#     @classmethod
#     def operate_sheet(cls, file_full_name, callback):
#         excel = cls.operate(file_full_name, cls.__get_excel)
#
#     @staticmethod
#     def __get_excel(excel):
#         return excel
