"""
 * @file   : test_Excel.py
 * @time   : 8:28
 * @date   : 2022/3/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.objectHelper import ObjectHelper
from hilandBasicLibrary.data.randomHelper import RandomHelper
from hilandBasicLibrary.io.fileHelper import FileHelper
from hilandBasicLibrary.io.pathHelper import PathHelper
# from hilandBasicLibrary.office.excelHelper import ExcelHelper
from hilandBasicLibrary.office.excelBookMate import ExcelBookMate


# def get_copied_excel_file():
#     source_file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
#     target_dir_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\target"
#     target_file_base_name = RandomHelper.create() + ".xlsx"
#     target_file_full_name = PathHelper.combine(target_dir_full_name, target_file_base_name)
#
#     FileHelper.copy(source_file_full_name, target_dir_full_name, target_file_base_name)
#     return target_file_full_name




# def test_open():
#     file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
#     excel = ExcelHelper.open(file_full_name)
#
#     actual = ObjectHelper.is_instance(excel, ExcelBookMate)
#     expected = True
#     assert actual == expected
