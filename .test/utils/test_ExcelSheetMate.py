"""
 * @file   : test_HilandSheet.py
 * @time   : 17:37
 * @date   : 2022/3/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from _res.usingLocalExcelCopied import UsingLocalExcelCopied
from BasicLibrary.data.randomHelper import RandomHelper
from BasicLibrary.io.fileHelper import FileHelper
from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.office.excelBookMate import ExcelBookMate
from BasicLibrary.projectHelper import ProjectHelper as ph


def test_get_row_column_count():
    source_file_full_name = PathHelper.combine(ph.get_root_physical_path(), r".test\_res\source\myExcel.xlsx")
    target_dir_full_name = PathHelper.combine(ph.get_root_physical_path(), r".test\_res\target")
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


def test_read():
    source_file_full_name = PathHelper.combine(ph.get_root_physical_path(), r".test\_res\source\yourExcel.xlsx")
    book_mate = ExcelBookMate(source_file_full_name)
    sheet_mate = book_mate.get_sheet(0)
    sheet_content = sheet_mate.read()
    actual = sheet_content
    expected = [['姓名', '年龄', '班级', '成绩'],
                ['张三', 20.0, '一', 88.0],
                ['李四', 19.0, '二', 89.0],
                ['王五', 21.0, '一', 59.0],
                ['赵六', 20.0, '三', 78.0]]
    assert actual == expected
    pass


def test_get_set():
    source_file_full_name = PathHelper.combine(ph.get_root_physical_path(), r".test\_res\source\myExcel.xlsx")
    target_dir_full_name = PathHelper.combine(ph.get_root_physical_path(), r".test\_res\target")
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
    my_sheet.set(new_value, range_marker)
    actual = my_sheet.get(range_marker)
    expected = new_value
    assert actual == expected

    range_marker = "A3:A4"
    new_value = [["zhangsan"], ["lisi"]]
    my_sheet.set(new_value, range_marker)
    actual = my_sheet.get(range_marker)
    expected = ['zhangsan', 'lisi']
    assert actual == expected

    # 不指定marker的情况下，会缺省写入 A1
    new_value = "zhangsan"
    my_sheet.set(new_value)
    actual = my_sheet.get("A1")
    expected = new_value
    assert actual == expected

    # 不指定marker的情况下，会缺省从 A1 开始往后推断位置并写入
    range_marker = "A1:A2"
    new_value = [["zhangsan"], ["lisi"]]
    my_sheet.set(new_value)
    actual = my_sheet.get(range_marker)
    expected = ['zhangsan', 'lisi']
    assert actual == expected

    my_book.close()
    FileHelper.remove(target_file_full_name)


def test_rename():
    with UsingLocalExcelCopied() as excel:
        my_sheet = excel.get_sheet()
        my_sheet.rename("Table A")
        actual = my_sheet.get_name()
        expected = "Table A"
        assert actual == expected
    pass


def test_get_row_count():
    with UsingLocalExcelCopied() as excel:
        my_sheet = excel.get_sheet()
        actual = my_sheet.get_row_count()
        expected = 5
        assert actual == expected
    pass


def test_get_column_count():
    with UsingLocalExcelCopied() as excel:
        my_sheet = excel.get_sheet()
        actual = my_sheet.get_column_count()
        expected = 4
        assert actual == expected
    pass


def test_copy_paste():
    with UsingLocalExcelCopied() as excel:
        my_sheet = excel.get_sheet()
        actual = my_sheet.copy("A1:C2")
        my_sheet.paste("F10")
        expected = my_sheet.get("F10:H11")
        print(expected)
        assert actual == expected
    pass
