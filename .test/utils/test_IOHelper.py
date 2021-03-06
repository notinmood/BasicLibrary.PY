"""
 * @file   : test_IOHelper.py
 * @time   : 9:30
 * @date   : 2022/2/17
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.io.fileHelper import FileHelper
from hilandBasicLibrary.io.ioHelper import IOHelper
from hilandBasicLibrary.io.pathHelper import PathHelper


def test_get_safe_filename():
    expected = IOHelper.get_illegal_chars_in_file_system()
    actual = ['?', '*', '"', ':', '<', '>', '|', '\\', '/']
    assert actual == expected

    _filename = "我是一:个好|人吗?"
    _filename = IOHelper.get_safe_file_system_name(_filename)
    expected = '我是一_个好_人吗_'
    actual = _filename
    assert actual == expected


def test_remove():
    source_file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\aa.txt"
    target_dir_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\target\ABB"
    FileHelper.copy(source_file_full_name, target_dir_full_name)
    target_file_full_name = PathHelper.combine(target_dir_full_name, "aa.txt")
    print(target_file_full_name)

    path = "E:\\myworkspace\\BasicLibrary.PY\\.test\\_res\\target\\ABDXyEXG\\aab.txt"
    IOHelper.remove(path)
    actual = 0
    expected = 0
    assert actual == expected
