"""
 * @file   : test_PathHelper.py
 * @time   : 8:46
 * @date   : 2021/12/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.io.pathHelper import PathHelper


def test_combine():
    p1 = "M"
    p2 = "aa"
    p3 = "bb"
    p4 = "cc"

    actual = PathHelper.combine(p1, p2, p3, p4)
    expected = "M\\aa\\bb\\cc"
    assert actual == expected


def test_get_dir_name():
    p = "E:\\workspace\\Project-python\\Comprehensive.PY"
    actual = PathHelper.get_dir_name(p)
    expected = "E:\\workspace\\Project-python"
    assert actual == expected


def test_get_base_name():
    p = "E:\\workspace\\Project-python\\Comprehensive.PY"
    actual = PathHelper.get_file_base_name(p)
    expected = "Comprehensive.PY"
    assert actual == expected

