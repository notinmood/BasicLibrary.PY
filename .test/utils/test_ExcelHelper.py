"""
 * @file   : test_Excel.py
 * @time   : 8:28
 * @date   : 2022/3/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.office.excelHelper import ExcelHelper


def test_calc_range_marker():
    actual = ExcelHelper.calc_range_marker("AA12", 1, 2)
    expected = 'AC13'
    assert actual == expected

    actual = ExcelHelper.calc_range_marker("AA12:BB1", 1, 2)
    expected = 'AC13:BD2'
    assert actual == expected


def test_calc_cell_marker():
    actual = ExcelHelper.calc_cell_marker("AA12", 1, 2)
    expected = 'AC13'
    assert actual == expected

    actual = ExcelHelper.calc_cell_marker("A1", 1, 26)
    expected = 'AA2'
    assert actual == expected

    actual = ExcelHelper.calc_cell_marker("-A1u4", 1, 26)
    expected = 'AA2'
    assert actual == expected

    actual = ExcelHelper.calc_cell_marker("-A1:u4", 1, 26)
    expected = 'AA2'
    assert actual == expected


def test_calc_column_name():
    actual = ExcelHelper.calc_column_name("A", 3)
    expected = "D"
    assert actual == expected

    actual = ExcelHelper.calc_column_name("A", -1)
    expected = False
    assert actual == expected

    actual = ExcelHelper.calc_column_name("A", 25)
    expected = "Z"
    assert actual == expected

    actual = ExcelHelper.calc_column_name("A", 26)
    expected = "AA"
    assert actual == expected

    actual = ExcelHelper.calc_column_name("AA", 1)
    expected = "AB"
    assert actual == expected

    actual = ExcelHelper.calc_column_name("BC", 22)
    expected = "BY"
    assert actual == expected

    actual = ExcelHelper.calc_column_name("BC", 25)
    expected = "CB"
    assert actual == expected

    actual = ExcelHelper.calc_column_name("BB", 1)
    expected = "BC"
    assert actual == expected

    actual = ExcelHelper.calc_column_name("BB", -1)
    expected = "BA"
    assert actual == expected

    actual = ExcelHelper.calc_column_name("BBB", 1)
    expected = False
    assert actual == expected


def test_operate_book():
    file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
    ExcelHelper.operate(file_full_name, __callback_excel)


def __callback_excel(excel):
    sheet_name = excel.get_sheet().get_name()
    actual = sheet_name
    expected = "表A"
    assert actual == expected


def test_operate_sheet():
    file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\myExcel.xlsx"
    ExcelHelper.operate_sheet(file_full_name, __callback_sheet, 1)


def __callback_sheet(sheet):
    sheet_name = sheet.get_name()
    actual = sheet_name
    expected = "表B"
    assert actual == expected
