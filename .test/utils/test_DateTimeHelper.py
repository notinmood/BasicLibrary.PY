"""
 * @file   : test_DateTimeHelper.py
 * @time   : 16:26
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from datetime import datetime

from BasicLibrary.data.dateTimeHelper import DateTimeHelper


def test_get_string():
    """
    测试DateTimeHelper
    :return:
    """
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
    测试DateTimeHelper
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

    data = "20211011"
    actual = DateTimeHelper.convert_from_string(data)
    expected = datetime(2021, 10, 11)
    assert actual == expected

    data = "20211011152532"
    actual = DateTimeHelper.convert_from_string(data)
    expected = datetime(2021, 10, 11,15, 25, 32)
    assert actual == expected


def test_get_compact_date_time_string():
    """
    测试DateTimeHelper
    :return:
    """
    data = "2021-10-11 00:34:25"
    actual = DateTimeHelper.get_compact_date_time_string(data)
    expected = "20211011003425"
    assert actual == expected
    pass


def test_get_format():
    """
    测试DateTimeHelper.get_format
    :return:
    """
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


def test_get_weekday_cn():
    """
    测试DateTimeHelper
    :return:
    """
    data = "2023-9-12 00:34:25"
    actual = DateTimeHelper.get_weekday_cn(data)
    expected = "星期二"
    assert actual == expected

    data = DateTimeHelper.convert_from_string(data)
    actual = DateTimeHelper.get_weekday_cn(data)
    expected = "星期二"
    assert actual == expected

    data = "2023-9-13"
    actual = DateTimeHelper.get_weekday_cn(data)
    expected = "星期三"
    assert actual == expected


pass


def test_get_date_lunar1():
    """
    测试闰月
    :return:
    """
    data = "2023-10-23 00:34:25"
    actual = DateTimeHelper.get_lunar_string(data)
    expected = "癸卯年九月初九日"
    assert actual == expected


pass


def test_get_date_lunar2():
    """
    测试DateTimeHelper
    :return:
    """
    data = "2023-10-23 00:34:25"
    actual = DateTimeHelper.get_lunar_string(data, False)
    expected = "九月初九日"
    assert actual == expected


pass


def test_get_date_lunar3():
    """
    测试闰月
    :return:
    """
    data = "2023-3-23"
    actual = DateTimeHelper.get_lunar_string(data, True)
    expected = "癸卯年闰二月初二日"
    assert actual == expected


pass


def test_get_date_lunar4():
    """
    测试闰月
    :return:
    """
    data = "2023-3-23"
    actual = DateTimeHelper.get_lunar_string(data, False)
    expected = "闰二月初二日"
    assert actual == expected


pass


def test_get_date_lunar5():
    """
    测试闰月
    :return:
    """
    data = "2024-1-20"
    actual = DateTimeHelper.get_lunar_string(data, False)
    expected = "腊月初十日"
    assert actual == expected


def test_get_timestamp1():
    actual = DateTimeHelper.get_timestamp(None, 10.6) * 1_000_000
    actual = len(str(int(actual)))
    expected = 16
    assert actual == expected

    actual = len(str(DateTimeHelper.get_timestamp(None, 16)))
    # actual = DateTimeHelper.get_timestamp(None, 16)
    expected = 16
    assert actual == expected

    actual = len(str(DateTimeHelper.get_timestamp(None, 13)))
    # actual = DateTimeHelper.get_timestamp(None, 13)
    expected = 13
    assert actual == expected

    actual = len(str(DateTimeHelper.get_timestamp(None, 10)))
    # actual = DateTimeHelper.get_timestamp(None, 10)
    expected = 10
    assert actual == expected


pass
