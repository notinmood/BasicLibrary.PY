"""
 * @file   : ReflectHelper_test.py
 * @time   : 9:49
 * @date   : 2021/12/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.Environment.ReflectHelper import ReflectHelper


def test_get_method_name():
    actual = ReflectHelper.get_current_method_name()
    expected = test_get_method_name.__name__
    assert actual == expected


def test_get_current_file():
    actual = ReflectHelper.get_current_file_name()
    expected = __file__
    assert actual == expected
