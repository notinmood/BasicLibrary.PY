"""
 * @file   : test_IOHelper.py
 * @time   : 9:30
 * @date   : 2022/2/17
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.io.ioHelper import IOHelper


def test_get_safe_filename():
    expected = IOHelper.get_illegal_chars_in_file_system()
    actual = ['?', '*', '"', ':', '<', '>', '|', '\\', '/']
    assert actual == expected

    _filename = "我是一:个好|人吗?"
    _filename = IOHelper.get_safe_file_system_name(_filename)
    expected = '我是一_个好_人吗_'
    actual = _filename
    assert actual == expected
