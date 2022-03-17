"""
 * @file   : test_Excel.py
 * @time   : 8:28
 * @date   : 2022/3/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.office.excelHelper import ExcelHelper


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
