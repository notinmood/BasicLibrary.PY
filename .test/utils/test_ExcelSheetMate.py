"""
 * @file   : test_HilandSheet.py
 * @time   : 17:37
 * @date   : 2022/3/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from _res.usingCopiedExcel import UsingCopiedExcel
from hilandBasicLibrary.data.randomHelper import RandomHelper
from hilandBasicLibrary.io.fileHelper import FileHelper
from hilandBasicLibrary.io.pathHelper import PathHelper
from hilandBasicLibrary.office.excelBookMate import ExcelBookMate


def test_get_row_column_count():
    source_file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
    target_dir_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\target"
    target_file_base_name = RandomHelper.create() + ".xlsx"
    target_file_full_name = PathHelper.combine(target_dir_full_name, target_file_base_name)

    FileHelper.copy(source_file_full_name, target_dir_full_name, target_file_base_name)

    my_book = ExcelBookMate(target_file_full_name)
    my_sheet = my_book.get_sheet(0)

    actual = my_sheet.get_row_count()
    expected = 5
    assert actual == expected

    actual = my_sheet.get_column_count()
    expected = 4
    assert actual == expected

    my_book.close()
    FileHelper.remove(target_file_full_name)


def test_get_set():
    source_file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
    target_dir_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\target"
    target_file_base_name = RandomHelper.create() + ".xlsx"
    target_file_full_name = PathHelper.combine(target_dir_full_name, target_file_base_name)

    FileHelper.copy(source_file_full_name, target_dir_full_name, target_file_base_name)

    my_book = ExcelBookMate(target_file_full_name)
    my_sheet = my_book.get_sheet(0)

    range_marker = "A2"
    actual = my_sheet.get(range_marker)
    expected = "张三"
    assert actual == expected

    new_value = "zhangsan"
    my_sheet.set(range_marker, new_value)
    actual = my_sheet.get(range_marker)
    expected = new_value
    assert actual == expected

    range_marker = "A3:A4"
    new_value = [["zhangsan"], ["lisi"]]
    my_sheet.set(range_marker, new_value)
    actual = my_sheet.get(range_marker)
    expected = ['zhangsan', 'lisi']
    assert actual == expected

    my_book.close()
    FileHelper.remove(target_file_full_name)


def test_rename():
    with UsingCopiedExcel() as excel:
        my_sheet = excel.get_sheet()
        my_sheet.rename("Table A")
        actual = my_sheet.get_name()
        expected = "Table A"
        assert actual == expected


def test_get_row_count():
    with UsingCopiedExcel() as excel:
        my_sheet = excel.get_sheet()
        actual = my_sheet.get_row_count()
        expected = 5
        assert actual == expected


def test_get_column_count():
    with UsingCopiedExcel() as excel:
        my_sheet = excel.get_sheet()
        actual = my_sheet.get_column_count()
        expected = 4
        assert actual == expected
