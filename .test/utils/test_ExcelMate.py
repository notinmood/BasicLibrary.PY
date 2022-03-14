"""
 * @file   : test_HilandExcel.py
 * @time   : 11:34
 * @date   : 2022/3/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from xlwings import Sheet

from hilandBasicLibrary.data.objectHelper import ObjectHelper
from hilandBasicLibrary.io.fileHelper import FileHelper
from hilandBasicLibrary.io.pathHelper import PathHelper
from hilandBasicLibrary.office.excelMate import ExcelMate


def test_open():
    file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
    excel = __open_detail(file_full_name)
    excel.close()

    file_full_name = ""
    excel = __open_detail(file_full_name)
    excel.close()


def __open_detail(file_full_name):
    excel = ExcelMate(file_full_name)
    actual = ObjectHelper.is_instance(excel, ExcelMate)
    expected = True
    assert actual == expected

    return excel


def test_save():
    file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
    excel = __open_detail(file_full_name)
    target_file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\target\xyz.xlsx"
    excel.save(target_file_full_name)

    actual = PathHelper.determine_is_exist(target_file_full_name)
    expected = True
    assert actual == expected

    excel.close()
    FileHelper.remove(target_file_full_name)

    actual = PathHelper.determine_is_exist(target_file_full_name)
    expected = False
    assert actual == expected


def test_get_sheets_count():
    file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
    excel = ExcelMate(file_full_name)

    actual = excel.get_sheets_count()
    expected = 3
    assert actual == expected


def test_get_sheet():
    file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
    excel = ExcelMate(file_full_name)
    my_sheet = excel.get_sheet()

    actual = ObjectHelper.is_instance(my_sheet.original_sheet, Sheet)
    expected = True
    assert actual == expected

    actual = my_sheet.original_sheet.name
    expected = "表A"
    assert actual == expected

    my_sheet = excel.get_sheet("表B")
    actual = my_sheet.original_sheet.name
    expected = "表B"
    assert actual == expected
    excel.close()


def test_with():
    file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
    with ExcelMate(file_full_name) as excel:
        actual = excel.get_sheets_count()
        expected = 3
        assert actual == expected
