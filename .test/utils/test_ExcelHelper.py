"""
 * @file   : test_Excel.py
 * @time   : 8:28
 * @date   : 2022/3/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.objectHelper import ObjectHelper
from hilandBasicLibrary.office.excelHelper import ExcelHelper
from hilandBasicLibrary.office.excelBookMate import ExcelBookMate


def test_open():
    file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
    excel = ExcelHelper.open(file_full_name)

    actual = ObjectHelper.is_instance(excel, ExcelBookMate)
    expected = True
    assert actual == expected
