"""
 * @file   : ConfigHelper_test.py
 * @time   : 22:22
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from HilandBasicLibrary.ConfigHelper import *


def test_get_item():
    actual = ConfigHelper.get_config_item("db_mongodb", "host")
    expected = "localhost"
    assert actual == expected

    actual = ConfigHelper.get_config_item("project_data", "console_information_display_level", 8)
    expected = 100
    assert actual == expected

    """
    TODO：需要根据以下两个测试,调整代码至不抛出异常
    """

    # actual = ConfigHelper.get_config_item("project_data", "bar", 8)
    # expected = 8
    # assert actual == expected

    # actual = ConfigHelper.get_config_item("project_bar", "bar", 8)
    # expected = 8
    # assert actual == expected
    #
