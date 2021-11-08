"""
 * @file   : DateTimeHelper_test.py
 * @time   : 16:26
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from HilandBasicLibrary.data.DateTimeHelper import *


def test_get_string():
    data = datetime(2021, 10, 11, 3, 34, 25)
    actual = DateTimeHelper.get_string(data)
    expected = "2021-10-11 03:34:25"
    assert actual == expected

    actual = DateTimeHelper.get_string(data, "%y|%m|%d %H%M%S")
    expected = "21|10|11 033425"
    assert actual == expected

    actual = DateTimeHelper.get_standard_string(data)
    expected = "2021-10-11 03:34:25"
    assert actual == expected

    actual = DateTimeHelper.get_short_string(data)
    expected = "2021-10-11"
    assert actual == expected

    actual = DateTimeHelper.get_compact_string(data)
    expected = "20211011"
    assert actual == expected


def test_convert_from_string():
    """

    :return:
    """
    data = "2021-10-11 03:34:25"
    actual = DateTimeHelper.convert_from_string(data, "%Y-%m-%d %H:%M:%S")
    expected = datetime(2021, 10, 11, 3, 34, 25)
    assert actual == expected

    data = "2021-10-11 03:34:25"
    actual = DateTimeHelper.convert_from_string(data)
    expected = datetime(2021, 10, 11, 3, 34, 25)
    assert actual == expected

    data = "2021-10-11"
    actual = DateTimeHelper.convert_from_string(data)
    expected = datetime(2021, 10, 11)
    assert actual == expected


def test_get_format():
    data = "2021-10-11 00:34:25"
    expected = "%Y-%m-%d %H:%M:%S"
    actual = DateTimeHelper.get_format(data)
    assert actual == expected

    data = "21-10-11 00:34:25"
    expected = "%y-%m-%d %H:%M:%S"
    actual = DateTimeHelper.get_format(data)
    assert actual == expected

    data = "20211011003425"
    expected = "%Y%m%d%H%M%S"
    actual = DateTimeHelper.get_format(data)
    assert actual == expected

    data = "2021-10-11"
    expected = "%Y-%m-%d"
    actual = DateTimeHelper.get_format(data)
    assert actual == expected

    data = "20211011"
    expected = "%Y%m%d"
    actual = DateTimeHelper.get_format(data)
    assert actual == expected

    data = "211011"
    expected = "%y%m%d"
    actual = DateTimeHelper.get_format(data)
    assert actual == expected
