"""

"""
from hilandBasicLibrary.office.excelBookMate import ExcelBookMate

# TODO:xiedali@2022/3/14 使用回调完善 ExcelHelper 功能
# class ExcelHelper:
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
