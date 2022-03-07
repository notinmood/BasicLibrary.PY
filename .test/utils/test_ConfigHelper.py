"""
 * @file   : test_ConfigHelper.py
 * @time   : 22:22
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.configHelper import *


def test_get_item0():
    actual = ConfigHelper.get_item("db_mysql", "insert_count_at_once", 200)
    expected = 100
    assert actual == expected


def test_get_item1():
    actual = ConfigHelper.get_item("db_mongodb", "host")
    expected = "localhost"
    assert actual == expected

    """
    验证缺省值
    """
    actual = ConfigHelper.get_item("project_data", "console_information_display_level", 8)
    expected = 100
    assert actual == expected

    """
    检索被.env覆写 section下的key
    """
    actual = ConfigHelper.get_item("db_mongodb", "database")
    expected = "stocks"
    assert actual == expected

    """
    检索不存在的key
    """
    actual = ConfigHelper.get_item("project_data", "bar", 8)
    expected = 8
    assert actual == expected

    """
    检索不存在的section
    """
    actual = ConfigHelper.get_item("project_bar", "bar", 8)
    expected = 8
    assert actual == expected
