"""
 * @file   : usingCopiedExcel.py
 * @time   : 10:32
 * @date   : 2022/3/15
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.randomHelper import RandomHelper
from hilandBasicLibrary.io.fileHelper import FileHelper
from hilandBasicLibrary.io.pathHelper import PathHelper
from hilandBasicLibrary.office.excelBookMate import ExcelBookMate


class UsingCopiedExcel:
    def __init__(self):
        self.target_file_full_name = self.get_copied_excel_file()
        self.excel = ExcelBookMate(self.target_file_full_name)

    def __enter__(self):
        return self.excel

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.excel.close()
        FileHelper.remove(self.target_file_full_name)

    @staticmethod
    def get_copied_excel_file():
        source_file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
        target_dir_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\target"
        target_file_base_name = RandomHelper.create() + ".xlsx"
        target_file_full_name = PathHelper.combine(target_dir_full_name, target_file_base_name)

        FileHelper.copy(source_file_full_name, target_dir_full_name, target_file_base_name)
        return target_file_full_name
