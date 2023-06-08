"""
 * @file   : test_IOHelper.py
 * @time   : 9:30
 * @date   : 2022/2/17
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.io.fileHelper import FileHelper
from BasicLibrary.io.ioHelper import IOHelper
from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.projectHelper import ProjectHelper


def test_get_file_system_safe_name1():
    expected = IOHelper.get_illegal_chars_in_file_system()
    actual = ['?', '*', '"', ':', '<', '>', '|', '\\', '/']
    assert actual == expected

    _filename = "我是一:个好|人吗?"
    _filename = IOHelper.get_file_system_safe_name(_filename)
    expected = '我是一_个好_人吗_'
    actual = _filename
    assert actual == expected


def test_get_file_system_safe_name2():
    _filename = "我🏮是✔️一:个好|人吗?"
    _filename = IOHelper.get_file_system_safe_name(_filename)
    expected = '我_是_一_个好_人吗_'
    actual = _filename
    assert actual == expected



def test_remove():
    source_file_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\source\aa.txt")
    target_dir_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\target\ABB")
    FileHelper.copy(source_file_full_name, target_dir_full_name)
    target_file_full_name = PathHelper.combine(target_dir_full_name, "aa.txt")
    print(target_file_full_name)

    path = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\\_res\\target\\ABDXyEXG\\aab.txt")
    IOHelper.remove(path)
    actual = 0
    expected = 0
    assert actual == expected
