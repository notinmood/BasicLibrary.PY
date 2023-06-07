"""
 * @file   : test_HilandExcel.py
 * @time   : 11:34
 * @date   : 2022/3/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from xlwings import Sheet

from BasicLibrary.projectHelper import ProjectHelper
from _res.usingCopiedExcel import UsingCopiedExcel
from BasicLibrary.data.objectHelper import ObjectHelper
from BasicLibrary.io.fileHelper import FileHelper
from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.office.excelBookMate import ExcelBookMate


def test_open():
    file_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\source\myExcel.xlsx")
    excel = __open_detail(file_full_name)
    excel.close()

    file_full_name = ""
    excel = __open_detail(file_full_name)
    excel.close()


def __open_detail(file_full_name):
    excel = ExcelBookMate(file_full_name)
    actual = ObjectHelper.is_instance(excel, ExcelBookMate)
    expected = True
    assert actual == expected

    return excel


def test_save():
    file_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\source\myExcel.xlsx")
    excel = __open_detail(file_full_name)
    target_file_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\target\xyz.xlsx")
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
    with UsingCopiedExcel() as excel:
        actual = excel.get_sheets_count()
        expected = 3
        assert actual == expected


def test_get_sheet():
    with UsingCopiedExcel() as excel:
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


def test_with():
    file_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\source\myExcel.xlsx")
    with ExcelBookMate(file_full_name) as excel:
        actual = excel.get_sheets_count()
        expected = 3
        assert actual == expected


def test_add_sheet1():
    with UsingCopiedExcel() as excel:
        excel.add_sheet("第四个表")
        actual = excel.get_sheets_count()
        expected = 4
        assert actual == expected
        actual = excel.get_sheet(3).original_sheet.name
        expected = "第四个表"
        assert actual == expected


def test_add_sheet2():
    with UsingCopiedExcel() as excel:
        excel.add_sheet("WPS", 3)
        for key in excel.get_sheets():
            print(key.original_sheet.name)

        actual = excel.get_sheets_count()
        expected = 4
        assert actual == expected
        actual = excel.get_sheet(3).original_sheet.name
        expected = "WPS"
        assert actual == expected


def test_add_sheet3():
    with UsingCopiedExcel() as excel:
        new_sheet = excel.add_sheet("我的yop", 4)

        actual = new_sheet.get_name()
        expected = "我的yop"
        assert actual == expected

        for key in excel.get_sheets():
            print(key.original_sheet.name)

        actual = excel.get_sheets_count()
        expected = 4
        assert actual == expected
        actual = excel.get_sheet(3).original_sheet.name
        expected = "我的yop"
        assert actual == expected

        actual = excel.get_sheet(4).original_sheet.name
        expected = "我的yop"
        assert actual == expected


def test_exist_sheet():
    with UsingCopiedExcel() as excel:
        actual = excel.determine_exist_sheet(0)
        expected = True
        assert actual == expected

        actual = excel.determine_exist_sheet(10)
        expected = False
        assert actual == expected

        actual = excel.determine_exist_sheet("表A")
        expected = True
        assert actual == expected

        actual = excel.determine_exist_sheet("表C")
        expected = False
        assert actual == expected


def test_remove_sheet():
    with UsingCopiedExcel() as excel:
        excel.remove_sheet("表A")
        actual = excel.get_sheets_count()
        expected = 2
        assert actual == expected

        excel.remove_sheet(0)
        actual = excel.get_sheets_count()
        expected = 1
        assert actual == expected

        excel.remove_sheet(10)
        actual = excel.get_sheets_count()
        expected = 1
        assert actual == expected

        excel.remove_sheet("其他不存在的表名称")
        actual = excel.get_sheets_count()
        expected = 1
        assert actual == expected

        excel.remove_sheet(0)
        actual = excel.get_sheets_count()
        expected = 1
        assert actual == expected


def test_rename_sheet():
    with UsingCopiedExcel() as excel:
        actual = excel.rename_sheet("表A", "Table A")
        expected = True
        assert actual == expected

        my_sheet = excel.get_sheet()
        actual = my_sheet.get_name()
        expected = "Table A"
        assert actual == expected

        my_sheet = excel.get_sheet(1)
        actual = my_sheet.get_name()
        expected = "表B"
        assert actual == expected

        actual = excel.rename_sheet("表P", "Table P")
        expected = False
        assert actual == expected


def test_copy_paste():
    with UsingCopiedExcel() as excel:
        actual = excel.copy(0, "A1:C2")
        excel.paste("表B", "F10")
        expected = excel.get_sheet("表B").get("F10:H11")
        print(expected)
        assert actual == expected
