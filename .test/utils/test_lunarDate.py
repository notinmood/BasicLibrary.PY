"""
 * @file   : test_lunarDate.py
 * @time   : 下午3:44
 * @date   : 2024/4/15
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.lunarDate import LunarDate


def test_func_name():
    lunar_date = LunarDate(2024, 4, 15)

    actual = lunar_date.year
    expected = "甲辰"
    assert actual == expected

    actual = lunar_date.month
    expected = "三"
    assert actual == expected

    actual = lunar_date.day
    expected = "初七"
    assert actual == expected
